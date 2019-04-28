#! /usr/bin/env bash
# echo "this is a test shell with arguments"
# echo "arg1 = $1; arg2 = $2;"
#清空Fastfile 文件内容
> /Users/haoli/Desktop/lottery/fastlane/Fastfile

#填充 Fastfile 文件内容
echo "default_platform(:ios)
platform :ios do
  desc ‘ipa打包’
  lane :Lottery do
    register_devices(
      devices: {
       '$1' => '$2',
      }
    ) 
    sigh(adhoc:true, force:true)  #如果要使用ad-hoc打包, 则需打开此项配置
    resign(
      bundle_id:'com.Chat.FlyBirdIM',
      ipa:'/Users/haoli/Desktop/fastlane_ipa/Lottery/Lottery.ipa', # can omit if using the `ipa` action
      signing_identity:'iPhone Distribution: Li Tongming (K25843MQW5)',
      # provisioning_profile: '/Users/haoli/Desktop/lottery/AdHoc_com.companyTest.test.mobileprovision', # can omit if using the _sigh_ action
    )
   end
end" >> /Users/haoli/Desktop/lottery/fastlane/Fastfile 


cd /Users/haoli/Desktop/lottery

# 解决没有授权 删除文件夹的权限  _floatsignTemp 签包时创建的临时文件夹
if [ -d "_floatsignTemp" ];then
echo "文件夹存在"
echo "lihao" | sudo -S rm -rf _floatsignTemp
else
echo "文件夹不存在"
fi

# 注册设备
fastlane Lottery





