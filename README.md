# Under the Spotlight: Web Tracking in Indian Partisan News Websites

Vibhor Agarwal, Yash Vekaria, Pushkal Agarwal, Sangeeta Mahapatra, Shounak Set, Sakthi Balan Muthiah, Nishanth Sastry, Nicolas Kourtellis, "Under the Spotlight: Web Tracking in Indian Partisan News Websites", AAAI 15th International Conference on Web and Social Media (ICWSM), 2021.

<div align="center">
  <img src="https://github.com/vibhor98/Web-Tracking-in-Indian-Partisan-News-Websites/blob/main/images/project_logo.png" width="500" height="300">
</div>

## Abstract
India is experiencing intense political partisanship and sectarian divisions. The paper performs, to the best of our knowledge, the first comprehensive analysis on the Indian online news media with respect to tracking and partisanship. We build a dataset of 103 online, mostly mainstream news websites. With the help of two experts, alongside data from the Media Ownership Monitor of the Reporters without Borders, we label these websites according to their partisanship (Left, Right, or Centre). We study and compare user tracking on these sites with different metrics: numbers of cookies, cookie synchronizations, device fingerprinting, and invisible pixelbased tracking. We find that Left and Centre websites serve more cookies than Right-leaning websites. However, through cookie synchronization, more user IDs, are synchronized in Left websites than Right or Centre. Canvas fingerprinting is used similarly by Left and Right, and less by Centre. Invisible pixel-based tracking is 50% more intense in Centre-leaning websites than Right, and 25% more than Left. Desktop versions of news websites deliver more cookies than their mobile counterparts. A handful of third-parties are tracking users in most websites in this study. This paper, by demonstrating intense web tracking, has implications for research on overall privacy of users visiting partisan news websites in India.

The paper PDF is available [here](https://arxiv.org/pdf/2102.03656.pdf). Our research is also covered in [The Open Magazine](https://openthemagazine.com/feature/tracking-the-trackers/).

**Note: The labelled dataset of Indian News Websites and crawls using these scripts can be requested from our dataset page [https://nms.kcl.ac.uk/netsys/datasets/india-tracking/](https://nms.kcl.ac.uk/netsys/datasets/india-tracking/) (Please abide to our listed T&C).**

We extend an existing crawling tool with our methodology, and open source our framework and dataset in order to promote further research and enable fellow researchers, policy makers, and even end-users to further inspect Indian news websites on the basis of tracking and partisanship.

## Methodology

<div align="center">
  <img src="https://github.com/vibhor98/Web-Tracking-in-Indian-Partisan-News-Websites/blob/main/images/HPWModel.png" width="900" height="400">
</div>

* `Dataset Curation` folder contains crawling scripts used in curating the news websites' list and dataset.
* `Cookie Analysis` folder contains analysis scripts used in cookie-based tracking analysis.
* `Cookie Synchronization` folder contains analysis scripts used in cookie synchronization.
* `Device Fingerprinting` folder contains analysis scripts used in device fingerprinting analysis.
* `Invisible Pixels` folder contains analysis scripts used in invisible pixel-based tracking analysis.

## Citation
If you find this paper useful in your research, please consider citing:
```
@inproceedings{agarwal2021spotlight,
title={Under the Spotlight: Web Tracking in Indian Partisan News Websites},
author={Vibhor Agarwal and Yash Vekaria and Pushkal Agarwal and Sangeeta Mahapatra and Shounak Set and Sakthi Balan Muthiah and Nishanth Sastry and Nicolas Kourtellis},
booktitle={Proceedings of the AAAI 15th International Conference on Web and Social Media (ICWSM)},
year={2021}
}
```
