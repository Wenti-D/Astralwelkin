![README_assets/Astralwelkin.svg](https://socialify.git.ci/Wenti-D/Astralwelkin/image?description=1&font=Inter&issues=1&logo=https%3A%2F%2Fraw.githubusercontent.com%2FWenti-D%2FAstralwelkin%2Fmain%2FREADME_assets%2FAstralwelkin.svg&name=1&owner=1&pulls=1&stargazers=1&theme=Dark)

## 这是什么？

「星天」，一个根据作者输入习惯制作的暗色[同文输入法](https://github.com/osfans/trime)主题，适合夜间使用，虽说还是有一个亮色配色的啦。

（甚至附带了一个全是 bug 的日文十二键输入法。）

## 这里有什么？

- `tools`：处理词典所用脚本
- `rime`：本项目的主要部分
  - `lua`：lua 脚本文件夹（目前里面只有日文用的）
  - `星天.trime.yaml`：主题本体
  - `bopomofo.custopm.yaml`：用于注音的配套设置
  - `double_pinyin_mspy.custom.yaml`：用于微软双拼的配套设置
  - `japanese_12_key.dict.yaml`：日文十二键用词库
  - `japanese_12_key.schema.yaml`：日文十二键输入方案
  - `japanese.dict.7z`：日文子词库压缩包
  - `luna_pinyin.custom.yaml`：用于朙月拼音的配套设置
  - `rime.lua`：Rime 输入法用到的 lua 脚本
- `dict_source.7z`：日文词典源文件与处理后的词库

## 长什么样？

<img src="README_assets/Screenshot_20220619_200033.jpg" width=500>

<img src="README_assets/Screenshot_20220619_200058.jpg" width=500>

<img src="README_assets/Screenshot_20220619_200108.jpg" width=500>

## 怎么用？

### 下载用到的字体

本主题所用的主要字体是 MiSans Regular，可以在[它的官网](https://hyperos.mi.com/font/zh/download/)下载到；扩展字体是遍黑体 P1 allideo，可以前往其[项目地址](https://github.com/Fitzgerald-Porthmouth-Koenigsegg/Plangothic-Project)下载。

> 之前本主题使用的是思源黑体，但实测思源系列字体（包括其衍生版）会让候选列表行距巨大，迫不得已改用 MiSans。
> 为什么不用 HarmonyOS Sans 呢？因为官方放出来的版本只有 BMP（U+0000 至 U+FFFF）范围，对我来说显然不够用。

### 将它放到你的设备上

想要哪些内容？

- 我全都要！
  1. 将本项目克隆到一个合适的位置；
  2. 将 `japanese.dict.7z` 里面的词库解压到 `rime` 文件夹下；
  3. 将前文所述的字体文件放入 `rime/fonts` 文件夹下； 
  4. 将 `rime` 文件夹与设备上的 `rime` 文件夹合并，再重新部署即可。
- 我不用日文
  1. 将本项目克隆到一个合适的位置；
  2. 去掉 `rime` 文件夹下以 `japanese` 开头的文件以及 lua 脚本；
  3. 将前文所述的字体文件放入 `rime/fonts` 文件夹下； 
  4. 将 `rime` 文件夹与设备上的 `rime` 文件夹合并，再重新部署即可。

**注意：如果目录下已经存在 `*.custom.yaml` 的话，建议手动修改合并文件内容。**

**警告：由于日文词库巨大，部署时间可能长达几分钟，期间部署界面很可能会出现卡顿**

### 按键说明

本主题在键上大量运用了滑动操作。

- 键上方的小字符号由长按输入；
- 键下方若只有一组符号，则通过下滑该键输入；
- 键下方若有左右两组符号，则通过左滑、右滑该键输入。

建议在设置中将「触发滑动手势的最短距离」适当调低些。

## 以后可能会有什么？

### 主题本体

- [ ] 增加颜文字输入键盘（对应现在没有作用的「^_^」键）；
- [ ] 增加更多符号输入（例如 emoji，对应现在的「鸽了」）；
- [ ] （若有需要）增加不同种类输入法的键盘。

### 日文输入法

- [x] 解决退格键在选词过程中多删的问题；
- [x] 回车直出平假名，而非内部编码；
- [ ] 增加符号词库（例如输入「ほし」会出现「☆」「★」等等）；
- [ ] 扩展标点、符号输入（例如输入「=」会出现「≒」「≞」等等）；
- [ ] 输入预测（例如输入「あそ」会给出「遊ぶ」「遊び」等等）。

## FAQ

### 1. 键盘上面的「摆烂」「鸽了」是什么？

还没想好放什么 ~~（想好了也忘了）~~ ，欢迎提出建议！

### 2. 为什么没有 XXX？

可以提个 issue，当然自己动手然后提交 PR 更好。

### 3. 我有问题（建议）怎么办？

可以提个 issue 或者发个邮件。
