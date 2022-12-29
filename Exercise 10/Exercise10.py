import ftplib
import setting.ftp as settings

ftp = ftplib.FTP(settings.FTP['URL'])
ftp.login()
ftp.cwd(settings.FTP["PATH"])
ftp.retrbinary("RETR " + settings.FTP["FILENAME"], open(settings.FTP["FILENAME"], 'wb').write)
ftp.quit()