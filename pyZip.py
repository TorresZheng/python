import os,os.path
import zipfile
import shutil
#
#win下ok
zipFinishFlag='0'
copyFinishFlag='0'
#文件复制
def moveFileto(sourceDir,  targetDir):
    shutil.copyfile(sourceDir,targetDir)
#文件压缩
def zip_dir(dirname,zipfilename):
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else :
        for root, dirs, files in os.walk(dirname):
            for name in files:
                filelist.append(os.path.join(root, name))
    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        #print arcname
        zf.write(tar,arcname)
    zf.close()
#打包成功后开始进行复制
    zipFinishFlag='1'
    if zipFinishFlag=='1':
        moveFileto('D:\\sd111.rar','E:\\sd111.rar')
        copyFinishFlag='1'
    else:
        return
#复制成功后删除原压缩文件，及文件夹
    if copyFinishFlag=='1':
        #递归删除文件夹
        shutil.rmtree(r'D:\\aqsiq')
        #删除单个文件
        os.remove('D:\\sd111.rar')
#  shutil.copyfile: 如何复制文件
#  os.path.exists: 如何判断文件夹是否存在
#  shutil.copytree: 如何复制目录树
zip_dir('D:\\aqsiq','D:\\sd111.rar')