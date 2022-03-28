import unittest 
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa=Kassapaate()
        self.kortti=Maksukortti(1000)
    def test_rahamaara_oikea(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    def test_myytyjen_edullisten_lounaiden_maara_oikea(self):
        self.assertEqual(self.kassa.edulliset, 0)
    def test_myytyjen_maukkaiden_lounaiden_maara_oikea(self):
        self.assertEqual(self.kassa.maukkaat, 0)
    def test_maksun_ollessa_riittava_kassassa_oleva_rahamaara_kasvaa_oikein_kateisella(self):
        self.kassa.syo_edullisesti_kateisella(250)
        self.kassa.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassa.kassassa_rahaa, 100640)
    def test_kun_ostetaan_edullinen_niin_vaihtoraha_oikein_kun_tarpeeksi_rahaa_kateisella(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(250),10)
    def test_kun_ostetaan_maukas_niin_vaihtoraha_oikein_kun_tarpeeksi_rahaa_kateisella(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(450),50)
    def test_myytyjen_edullisten_lounaiden_maara_kasvaa_oikein_kun_tarpeeksi_rahaa_kateisella(self):
        self.kassa.syo_edullisesti_kateisella(250)
        self.kassa.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassa.edulliset,2)
    def test_myytyjen_maukkaiden_lounaiden_maara_kasvaa_oikein_kun_tarpeeksi_rahaa_kateisella(self):
        self.kassa.syo_maukkaasti_kateisella(450)
        self.kassa.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassa.maukkaat,2)
    def test_jos_kateisella_maksu_ei_ole_riittava_niin_kassassa_oleva_rahamaara_ei_muutu(self):
        self.kassa.syo_maukkaasti_kateisella(250)
        self.kassa.syo_maukkaasti_kateisella(250)
        self.assertEqual(self.kassa.kassassa_rahaa,100000)
    def test_jos_kateisella_maksu_ei_ole_riittava_niin_kaikki_rahat_palautetaan_vaihtorahana(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(250), 250)
    def test_jos_kateisella_maksu_ei_ole_riittava_niin_myytyjen_edullisten_lounaiden_maara_ei_muutu(self):
        self.kassa.syo_edullisesti_kateisella(150)
        self.assertEqual(self.kassa.edulliset,0)
    def test_jos_kateisella_maksu_ei_ole_riittava_niin_myytyjen_maukkaiden_lounaiden_maara_ei_muutu(self):
        self.kassa.syo_maukkaasti_kateisella(150)
        self.assertEqual(self.kassa.maukkaat,0)
    

    def test_kun_ostetaan_edullinen_niin_veloitetaan_oikea_summa_kun_tarpeeksi_rahaa_kateisella(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti),"saldo: 7.6")

    def test_kun_ostetaan_maukas_niin_veloitetaan_oikea_summa_kun_tarpeeksi_rahaa_kateisella(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti),"saldo: 6.0")
    def test_kun_ostetaan_edullinen_niin_palautetaan_True_kun_tarpeeksi_rahaa_kateisella(self):
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti),True)
    def test_kun_ostetaan_maukas_niin_palautetaan_True_kun_tarpeeksi_rahaa_kateisella(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti),True)
    def test_jos_kortilla_on_tarpeeksi_rahaa_niin_myytyjen_edullisten_lounaiden_maara_kasvaa(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.kassa.syo_edullisesti_kortilla(self.kortti)  
        self.assertEqual(self.kassa.edulliset,2)      
    def test_jos_kortilla_on_tarpeeksi_rahaa_niin_myytyjen_maukkaiden_lounaiden_maara_kasvaa(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)  
        self.assertEqual(self.kassa.maukkaat,2)  
    def test_jos_kortilla_ei_tarpeeksi_rahaa_kortin_rahamaara_ei_muutu(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        #Kortilla saldoa jäljellä 2 euroa
        self.kassa.syo_edullisesti_kortilla(self.kortti)         
        self.assertEqual(str(self.kortti),"saldo: 2.0")
    def test_jos_kortilla_ei_tarpeeksi_rahaa_myytyjen_maukkaiden_lounaiden_maara_muuttumaton(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        #Kortilla saldoa jäljellä 2 euroa
        self.kassa.syo_maukkaasti_kortilla(self.kortti)  
        self.assertEqual(self.kassa.maukkaat,2)        
    def test_jos_kortilla_ei_tarpeeksi_rahaa_myytyjen_edullisten_lounaiden_maara_muuttumaton(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        #Kortilla saldoa jäljellä 2 euroa
        self.kassa.syo_edullisesti_kortilla(self.kortti)  
        self.assertEqual(self.kassa.edulliset,0)   
    def test_jos_kortilla_ei_tarpeeksi_rahaa_palautetaan_False(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        #Kortilla saldoa jäljellä 2 euroa
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti),False)  
    def test_kassassa_oleva_rahamaara_ei_muutu_kun_ostetaan_kortilla(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)   
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    def test_kortin_saldo_muuttuu_ladatulla_summalla(self):
        self.kassa.lataa_rahaa_kortille(self.kortti,1000)
        self.assertEqual(str(self.kortti),"saldo: 20.0")
    def test_kassassa_oleva_rahamaara_kasvaa_ladatulla_summalla(self):
        self.kassa.lataa_rahaa_kortille(self.kortti,1000)
        self.assertEqual(self.kassa.kassassa_rahaa,101000)


    def test_jos_ladataan_negatiivinen_maara_rahaa_kortille_niin_saldo_ei_muutu(self):
        self.kassa.lataa_rahaa_kortille(self.kortti,-1000)
        self.assertEqual(str(self.kortti),"saldo: 10.0")   

    def test_jos_ladataan_negatiivinen_maara_rahaa_kortille_niin_kassan_rahamaara_ei_muutu(self):
        self.kassa.lataa_rahaa_kortille(self.kortti,-1000)
        self.assertEqual(self.kassa.kassassa_rahaa,100000)     