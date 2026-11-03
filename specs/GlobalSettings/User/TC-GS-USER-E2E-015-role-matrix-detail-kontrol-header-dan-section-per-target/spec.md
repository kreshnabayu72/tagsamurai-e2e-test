---
id: TC-GS-USER-E2E-015-role-matrix-detail-kontrol-header-dan-section-per-target
title: "Role Matrix: Kontrol Header dan Section User Detail untuk Aktor Total Control dan Full CRUD terhadap Target Default User, Self, Tier Total Control, Tier Read Only, dan Normal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-74
  - TC-GS-USER-75
  - TC-GS-USER-76
  - TC-GS-USER-77
  - TC-GS-USER-78
  - TC-GS-USER-79
  - TC-GS-USER-80
coverage:
  web: automated
---

# Role Matrix: Kontrol Header dan Section User Detail untuk Aktor Total Control dan Full CRUD terhadap Target Default User, Self, Tier Total Control, Tier Read Only, dan Normal

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Role yang diuji (tiap role memakai akunnya sendiri; langkah ganti akun ditulis eksplisit di Test Steps):

| Role | Akun (Tabel Data Uji Pre-setup) | Nama user | Env var password | Target yang diuji |
|---|---|---|---|---|
| Total Control | `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (No. 2) | Siti Nurhaliza | `Spectra.env.GS_TC_PASSWORD` | Default User (TC-GS-USER-74), Self (TC-GS-USER-75) |
| Manage user and role (Full CRUD) | `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net` (No. 4) | Fajar Nugroho | `Spectra.env.GS_FULLCRUD_PASSWORD` | Tier Total Control (TC-GS-USER-76), Tier Read Only (TC-GS-USER-77), Normal (TC-GS-USER-78), Self (TC-GS-USER-79), Default User (TC-GS-USER-80) |

- Login akun Total Control (aktor pertama spec, sekaligus akun default suite) dilakukan di hook `before`; Full CRUD memakai langkah ganti akun eksplisit. Karena spec berakhir di akun Full CRUD, hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`, `GS_FULLCRUD_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup, hanya dibaca; spec tidak membuat, mengubah, atau menghapus data): Hendra Gunawan (No. 1, Default User, MFA Enrolled), Andi Wijaya (No. 10, tier Total Control), Doni Pratama (No. 11, tier Read Only), Dewi Lestari (No. 12, Normal, belum punya assignment Role sehingga switch Active Tab Role OFF dan checkbox C/U/D disabled; TC-GS-USER-78 e), Custom Field `Blood Type` (No. 24), akun aktor Siti Nurhaliza dan Fajar Nugroho (No. 2 dan 4). Siti Nurhaliza berstatus MFA Enrolled (diperlukan agar button `Reset Authenticator` tampil pada TC-GS-USER-75; Tabel Pre-setup tidak menyebut status ini, disediakan tim FE). Client plan Growth (Pre-setup No. 26) agar `Scan TAG` tampil.
- Kemampuan teknis: hover elemen termasuk elemen disabled untuk membaca tooltip; membaca state tampil/Hidden dan enabled/disabled.
- State global yang diubah: tidak ada. Cleanup: tidak ada data dibuat; hook `after` hanya memulihkan sesi.

## Test Steps

### TC-GS-USER-74: Kontrol header dan section target Default User untuk aktor Total Control

1. Klik icon Search, ketik `Hendra Gunawan`, tekan Enter
2. Klik Name `Hendra Gunawan` untuk membuka Detail
3. Hover switch Active header
4. Verifikasi switch Active header tampil namun disabled
5. Verifikasi tooltip switch Active "Default User cannot be modified."
6. Klik menu `[⋯]` header
7. Verifikasi `Edit Profile` tampil dan enabled
8. Verifikasi `Delete User` tampil namun disabled
9. Hover `Delete User`
10. Verifikasi tooltip `Delete User` "Default User cannot be modified."
11. Tekan Esc untuk menutup menu `[⋯]`
12. Hover button `Reset Authenticator`
13. Verifikasi button `Reset Authenticator` tampil namun disabled
14. Verifikasi tooltip `Reset Authenticator` "Default User cannot be modified."
15. Verifikasi `Scan TAG`/`Unpair` tampil dan enabled
16. Hover baris Custom Field `Blood Type`
17. Verifikasi icon inline edit Custom Field tampil
18. Verifikasi icon inline edit Custom Field enabled
19. Klik Tab `Role`
20. Verifikasi keenam switch Active Tab Role ON
21. Hover switch Active Tab Role
22. Verifikasi switch Active Tab Role tampil namun disabled
23. Verifikasi tooltip switch Active Tab Role "Default User cannot be modified."
24. Verifikasi checkbox CRUD Tab Role disabled

### TC-GS-USER-75: Kontrol header dan section target Self untuk aktor Total Control

25. Klik menu User di sidebar Global Settings
26. Klik icon Search, ketik `Siti Nurhaliza`, tekan Enter
27. Klik Name `Siti Nurhaliza` (baris akun sendiri) untuk membuka Detail
28. Hover switch Active header
29. Verifikasi switch Active header tampil namun disabled
30. Verifikasi tooltip switch Active "You can't manage your own account from here."
31. Klik menu `[⋯]` header
32. Verifikasi `Edit Profile` tampil dan enabled
33. Verifikasi `Delete User` tampil namun disabled
34. Hover `Delete User`
35. Verifikasi tooltip `Delete User` "You can't manage your own account from here."
36. Tekan Esc untuk menutup menu `[⋯]`
37. Hover button `Reset Authenticator`
38. Verifikasi button `Reset Authenticator` tampil namun disabled
39. Verifikasi tooltip `Reset Authenticator` "Ask another admin to reset your authenticator."
40. Hover baris Custom Field `Blood Type`
41. Verifikasi icon inline edit Custom Field tampil dan enabled
42. Klik Tab `Role`
43. Hover switch Active Tab Role
44. Verifikasi switch Active Tab Role tampil namun disabled
45. Verifikasi tooltip switch Active Tab Role "You can't manage your own account from here."
46. Hover checkbox Tab Role
47. Verifikasi checkbox Tab Role tampil namun disabled
48. Verifikasi tooltip checkbox Tab Role "You can't manage your own account from here."
49. Hover Avatar header
50. Verifikasi `[Edit]` tampil pada Avatar header

### TC-GS-USER-76: Kontrol header dan section target Tier TC untuk aktor Full CRUD

51. Logout, login sebagai Manage user and role (Full CRUD), lalu buka Global Settings > User > User List (sub-tab Login User)
52. Klik icon Search, ketik `Andi Wijaya`, tekan Enter
53. Klik Name `Andi Wijaya` untuk membuka Detail
54. Hover switch Active header
55. Verifikasi switch Active header tampil namun disabled
56. Verifikasi tooltip switch Active "You don't have permission to edit."
57. Klik menu `[⋯]` header
58. Verifikasi `Edit Profile` dan `Delete User` tampil namun disabled
59. Hover `Edit Profile`
60. Verifikasi tooltip `Edit Profile` "You don't have permission to edit."
61. Hover `Delete User`
62. Verifikasi tooltip `Delete User` "You don't have permission to edit."
63. Tekan Esc untuk menutup menu `[⋯]`
64. Verifikasi sub-section User TAG tampil
65. Verifikasi `Scan TAG`, `Unpair`, dan `Resend Activation/Confirmation Email` Hidden
66. Hover baris Custom Field `Blood Type`
67. Hover icon inline edit Custom Field
68. Verifikasi icon inline edit Custom Field tampil namun disabled
69. Verifikasi tooltip icon inline edit "You don't have permission to edit."
70. Klik Tab `Role`
71. Hover switch Active Tab Role
72. Verifikasi switch Active Tab Role tampil namun disabled
73. Verifikasi tooltip switch Active Tab Role "You don't have permission to edit."
74. Hover checkbox Tab Role
75. Verifikasi checkbox Tab Role tampil namun disabled
76. Verifikasi tooltip checkbox Tab Role "You don't have permission to edit."

### TC-GS-USER-77: Kontrol header dan section target Tier RO untuk aktor Full CRUD

77. Klik menu User di sidebar Global Settings
78. Klik icon Search, ketik `Doni Pratama`, tekan Enter
79. Klik Name `Doni Pratama` untuk membuka Detail
80. Hover switch Active header
81. Verifikasi switch Active header tampil namun disabled
82. Verifikasi tooltip switch Active "You don't have permission to edit."
83. Klik menu `[⋯]` header
84. Verifikasi `Edit Profile` dan `Delete User` tampil namun disabled
85. Hover `Edit Profile`
86. Verifikasi tooltip `Edit Profile` "You don't have permission to edit."
87. Hover `Delete User`
88. Verifikasi tooltip `Delete User` "You don't have permission to edit."
89. Tekan Esc untuk menutup menu `[⋯]`
90. Verifikasi sub-section User TAG tampil
91. Verifikasi `Scan TAG` dan `Unpair` Hidden
92. Hover baris Custom Field `Blood Type`
93. Hover icon inline edit Custom Field
94. Verifikasi icon inline edit Custom Field tampil namun disabled
95. Verifikasi tooltip icon inline edit "You don't have permission to edit."
96. Klik Tab `Role`
97. Hover switch Active Tab Role
98. Verifikasi switch Active Tab Role tampil namun disabled
99. Verifikasi tooltip switch Active Tab Role "You don't have permission to edit."
100. Hover checkbox Tab Role
101. Verifikasi checkbox Tab Role tampil namun disabled
102. Verifikasi tooltip checkbox Tab Role "You don't have permission to edit."

### TC-GS-USER-78: Kontrol header dan section target Normal untuk aktor Full CRUD

103. Klik menu User di sidebar Global Settings
104. Klik icon Search, ketik `Dewi Lestari`, tekan Enter
105. Klik Name `Dewi Lestari` untuk membuka Detail
106. Verifikasi switch Active header enabled
107. Klik menu `[⋯]` header
108. Verifikasi `Edit Profile` dan `Delete User` enabled
109. Tekan Esc untuk menutup menu `[⋯]`
110. Verifikasi `Scan TAG` enabled
111. Hover baris Custom Field `Blood Type`
112. Verifikasi icon inline edit Custom Field enabled
113. Klik Tab `Role`
114. Verifikasi switch Active Tab Role enabled
115. Verifikasi checkbox C/U/D Tab Role disabled pada baris dengan switch OFF

### TC-GS-USER-79: Kontrol header dan section target Self untuk aktor Full CRUD

116. Klik menu User di sidebar Global Settings
117. Klik icon Search, ketik `Fajar Nugroho`, tekan Enter
118. Klik Name `Fajar Nugroho` (baris akun sendiri) untuk membuka Detail
119. Hover switch Active header
120. Verifikasi switch Active header tampil namun disabled
121. Verifikasi tooltip switch Active "You can't manage your own account from here."
122. Klik menu `[⋯]` header
123. Verifikasi `Edit Profile` tampil dan enabled
124. Verifikasi `Delete User` tampil namun disabled
125. Hover `Delete User`
126. Verifikasi tooltip `Delete User` "You can't manage your own account from here."
127. Tekan Esc untuk menutup menu `[⋯]`
128. Hover baris Custom Field `Blood Type`
129. Verifikasi icon inline edit Custom Field tampil dan enabled
130. Klik Tab `Role`
131. Hover switch Active Tab Role
132. Verifikasi switch Active Tab Role tampil namun disabled
133. Verifikasi tooltip switch Active Tab Role "You can't manage your own account from here."
134. Hover checkbox Tab Role
135. Verifikasi checkbox Tab Role tampil namun disabled
136. Verifikasi tooltip checkbox Tab Role "You can't manage your own account from here."
137. Hover Avatar header
138. Verifikasi `[Edit]` tampil pada Avatar header dan enabled

### TC-GS-USER-80: Kontrol header dan section target Default User untuk aktor Full CRUD

139. Klik menu User di sidebar Global Settings
140. Klik icon Search, ketik `Hendra Gunawan`, tekan Enter
141. Klik Name `Hendra Gunawan` untuk membuka Detail
142. Hover switch Active header
143. Verifikasi switch Active header tampil namun disabled
144. Verifikasi tooltip switch Active "Default User cannot be modified."
145. Klik menu `[⋯]` header
146. Verifikasi `Edit Profile` dan `Delete User` tampil namun disabled
147. Hover `Edit Profile`
148. Verifikasi tooltip `Edit Profile` "You don't have permission to edit."
149. Hover `Delete User`
150. Verifikasi tooltip `Delete User` "Default User cannot be modified."
151. Tekan Esc untuk menutup menu `[⋯]`
152. Hover baris Custom Field `Blood Type`
153. Hover icon inline edit Custom Field
154. Verifikasi icon inline edit Custom Field tampil namun disabled
155. Verifikasi tooltip icon inline edit "Default User cannot be modified."
156. Verifikasi sub-section User TAG tampil
157. Verifikasi `Scan TAG`/`Unpair` Hidden
158. Klik Tab `Role`
159. Verifikasi keenam switch Active Tab Role ON
160. Hover switch Active Tab Role
161. Verifikasi switch Active Tab Role tampil namun disabled
162. Verifikasi tooltip switch Active Tab Role "Default User cannot be modified."

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (162 langkah) karena ketujuh TC berada di satu kelas harness (Role Matrix visibilitas kontrol, bagian 3a) pada satu layar (User Detail), hanya membaca state dan tidak mengubah data; tiap blok TC membuka Detail targetnya sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Satu langkah `Verifikasi` per klausa Expected (state dan tooltip dipisah, S-01) membuat jumlah langkah besar.
- Urutan TC sumber dipertahankan (TC-GS-USER-74 dan 75 aktor Total Control, TC-GS-USER-76 sampai 80 aktor Full CRUD); tidak ada aksi yang menghapus atau mengubah data.
- Langkah buka layar User List untuk akun awal tidak ditulis di Test Steps: dibuka oleh `beforeEach` suite (`suite.md`); pembukaan User List setelah ganti akun menjadi bagian langkah 51 karena `beforeEach` tidak dijalankan ulang. Langkah penghubung (aksi tanpa `Verifikasi`): Search nama target sebelum membuka Detail pada tiap blok, menekan Esc untuk menutup menu `[⋯]`, ganti akun (langkah 51), klik Tab `Role` sebelum membaca switch dan checkbox Tab Role (langkah 4 TC menyebut Tab Role sebagai bagian yang diamati), dan hover baris Custom Field sebelum membaca icon inline edit yang muncul saat hover.
- Anchor absence (bagian 8b butir 2): `Verifikasi` "sub-section User TAG tampil" mendahului asersi `Scan TAG`/`Unpair` Hidden pada langkah 64, 90, dan 156; asersi ini tidak ada di TC dan ditambahkan hanya sebagai anchor. `Resend Activation/Confirmation Email` Hidden (TC-GS-USER-76 c) berada pada header Detail yang sama dengan switch Active yang sudah terverifikasi tampil.
- Langkah 5 TC (hover elemen yang disabled) dipenuhi di langkah hover masing-masing elemen sebelum `Verifikasi` tooltip (state sementara diasersi tepat waktu, bagian 8b butir 5).
- Pembagian TC lintas spec: hover Avatar `[Edit]` pada akun sendiri (TC-GS-USER-75 f dan TC-GS-USER-79 e) diverifikasi di spec ini; aksi unggah foto akun sendiri (TC-GS-USER-83) diverifikasi di spec 018.
- Temuan untuk QA:
  - TC-GS-USER-74 c ("Button `Reset Authenticator` (bila Enrolled)") dan TC-GS-USER-75 c tidak menyebut status MFA aktor/target di precondition; spec mensyaratkan Hendra Gunawan (Pre-setup No. 1) dan Siti Nurhaliza berstatus Enrolled.
  - TC-GS-USER-74 d dan TC-GS-USER-75 tidak menyebut kondisi TAG target (`Unpair` hanya relevan bila TAG terpasang, `Scan TAG` bila belum); TC-GS-USER-74 d mengharapkan `Scan TAG`/`Unpair` keduanya tampil dan enabled tanpa precondition TAG; spec mengasersi seperti tertulis.
  - TC-GS-USER-74 f menyebut "checkbox CRUD disabled" tanpa tooltip, sedangkan keenam switch Active disebut bertooltip; spec mengasersi tooltip hanya pada switch Active. TC-GS-USER-75 e, 76 e, 77 e, dan 79 d menyebut "Switch Active dan checkbox Tab Role" tanpa menunjuk baris; spec memakai baris pertama Tab Role.
  - TC-GS-USER-78 e mensyaratkan Dewi Lestari belum punya assignment (seluruh switch Active Tab Role OFF); Tabel Pre-setup No. 12 tidak menyebutnya.
  - TC-GS-USER-76 c menyebut `Resend Activation/Confirmation Email` Hidden tanpa menyebut status target (Andi Wijaya) yang membuat Resend relevan; asersi Hidden mengikuti TC.
  - TC-GS-USER-74 e dan TC-GS-USER-75 d menyebut "Icon inline edit Custom Field" tanpa menyebut field mana; spec memakai `Blood Type` (Pre-setup No. 24).
