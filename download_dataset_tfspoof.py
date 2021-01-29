import os

all_links = ['ftp://smartengines.com/midv-500/dataset/01_alb_id.zip',
             'ftp://smartengines.com/midv-500/dataset/02_aut_drvlic_new.zip',
             'ftp://smartengines.com/midv-500/dataset/03_aut_id_old.zip',
             'ftp://smartengines.com/midv-500/dataset/04_aut_id.zip',
             'ftp://smartengines.com/midv-500/dataset/05_aze_passport.zip', 
             'ftp://smartengines.com/midv-500/dataset/06_bra_passport.zip',
             'ftp://smartengines.com/midv-500/dataset/07_chl_id.zip',
             'ftp://smartengines.com/midv-500/dataset/08_chn_homereturn.zip',
             'ftp://smartengines.com/midv-500/dataset/09_chn_id.zip',
             'ftp://smartengines.com/midv-500/dataset/10_cze_id.zip',
             'ftp://smartengines.com/midv-500/dataset/11_cze_passport.zip',
             'ftp://smartengines.com/midv-500/dataset/12_deu_drvlic_new.zip',
             'ftp://smartengines.com/midv-500/dataset/13_deu_drvlic_old.zip',
             'ftp://smartengines.com/midv-500/dataset/14_deu_id_new.zip',
             'ftp://smartengines.com/midv-500/dataset/15_deu_id_old.zip',
             'ftp://smartengines.com/midv-500/dataset/16_deu_passport_new.zip',
             'ftp://smartengines.com/midv-500/dataset/17_deu_passport_old.zip',
             'ftp://smartengines.com/midv-500/dataset/18_dza_passport.zip',
             'ftp://smartengines.com/midv-500/dataset/19_esp_drvlic.zip',
             'ftp://smartengines.com/midv-500/dataset/20_esp_id_new.zip',
             'ftp://smartengines.com/midv-500/dataset/21_esp_id_old.zip',
             'ftp://smartengines.com/midv-500/dataset/22_est_id.zip',
             'ftp://smartengines.com/midv-500/dataset/23_fin_drvlic.zip',
             'ftp://smartengines.com/midv-500/dataset/24_fin_id.zip',
             'ftp://smartengines.com/midv-500/dataset/25_grc_passport.zip',
             'ftp://smartengines.com/midv-500/dataset/26_hrv_drvlic.zip',
             'ftp://smartengines.com/midv-500/dataset/27_hrv_passport.zip',
             'ftp://smartengines.com/midv-500/dataset/28_hun_passport.zip',
             'ftp://smartengines.com/midv-500/dataset/29_irn_drvlic.zip',
             'ftp://smartengines.com/midv-500/dataset/30_ita_drvlic.zip',
             'ftp://smartengines.com/midv-500/dataset/31_jpn_drvlic.zip',
             'ftp://smartengines.com/midv-500/dataset/32_lva_passport.zip',
             'ftp://smartengines.com/midv-500/dataset/33_mac_id.zip',
             'ftp://smartengines.com/midv-500/dataset/34_mda_passport.zip',
             'ftp://smartengines.com/midv-500/dataset/35_nor_drvlic.zip',
             'ftp://smartengines.com/midv-500/dataset/36_pol_drvlic.zip',
             'ftp://smartengines.com/midv-500/dataset/37_prt_id.zip',
             'ftp://smartengines.com/midv-500/dataset/38_rou_drvlic.zip',
             'ftp://smartengines.com/midv-500/dataset/39_rus_internalpassport.zip',
             'ftp://smartengines.com/midv-500/dataset/40_srb_id.zip',
             'ftp://smartengines.com/midv-500/dataset/41_srb_passport.zip',
             'ftp://smartengines.com/midv-500/dataset/42_svk_id.zip',
             'ftp://smartengines.com/midv-500/dataset/43_tur_id.zip',
             'ftp://smartengines.com/midv-500/dataset/44_ukr_id.zip',
             'ftp://smartengines.com/midv-500/dataset/45_ukr_passport.zip',
             'ftp://smartengines.com/midv-500/dataset/46_ury_passport.zip',
             'ftp://smartengines.com/midv-500/dataset/47_usa_bordercrossing.zip',
             'ftp://smartengines.com/midv-500/dataset/48_usa_passportcard.zip',
             'ftp://smartengines.com/midv-500/dataset/49_usa_ssn82.zip',
             'ftp://smartengines.com/midv-500/dataset/50_xpo_id.zip']
             
             
def main():
	
	for link in all_links:
		print('----------------------------------------------------------------------')
        	print('\nDownloading:', link[40:])
        	os.system('wget ' + link)
        	print('Downloaded:', link[40:])
        	print('Unzipping:', link[40:])
        	os.system('unzip ' + link[40:])
	

