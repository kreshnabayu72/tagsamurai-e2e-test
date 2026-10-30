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
- Data Pre-setup (Tabel Data Uji Pre-setup, hanya dibaca; spec tidak membuat, mengubah, atau menghapus data): Hendra Gunawan (No. 1, Default User, MFA Enrolled), Andi Wijaya (No. 10, tier Total Control), Doni Pratama (No. 11, tier Read Only), Dewi Lestari (No. 12, Normal), Custom Field `Blood Type` (No. 24), akun aktor Siti Nurhaliza dan Fajar Nugroho (No. 2 dan 4). Siti Nurhaliza berstatus MFA Enrolled (diperlukan agar button `Reset Authenticator` tampil pada TC-GS-USER-75; Tabel Pre-setup tidak menyebut status ini, disediakan tim FE). Client plan Growth (Pre-setup No. 26) agar `Scan TAG` tampil.
- Kemampuan teknis: hover elemen termasuk elemen disabled untuk membaca tooltip; membaca state tampil/Hidden dan enabled/disabled.
- State global yang diubah: tidak ada. Cleanup: tidak ada data dibuat; hook `after` hanya memulihkan sesi.

## Test Steps

### TC-GS-USER-74: Kontrol header dan section target Default User untuk aktor Total Control

1. Buka Global Settings > User > User List (sub-tab Login User)
2. Klik icon Search, ketik `Hendra Gunawan`, tekan Enter
3. Klik Name `Hendra Gunawan` untuk membuka Detail
4. Hover switch Active header
5. Verifikasi switch Active header tampil namun disabled
6. Verifikasi tooltip switch Active `"Default User cannot be modified."`
7. Klik menu `[⋯]` header
8. Verifikasi `Edit Profile` tampil dan enabled
9. Verifikasi `Delete User` tampil namun disabled
10. Hover `Delete User`
11. Verifikasi tooltip `Delete User` `"Default User cannot be modified."`
12. Tekan Esc untuk menutup menu `[⋯]`
13. Hover button `Reset Authenticator`
14. Verifikasi button `Reset Authenticator` tampil namun disabled
15. Verifikasi tooltip `Reset Authenticator` `"Default User cannot be modified."`
16. Verifikasi `Scan TAG`/`Unpair` tampil dan enabled
17. Hover baris Custom Field `Blood Type`
18. Verifikasi icon inline edit Custom Field tampil
19. Verifikasi icon inline edit Custom Field enabled

### TC-GS-USER-75: Kontrol header dan section target Self untuk aktor Total Control

20. Klik menu User di sidebar Global Settings
21. Klik icon Search, ketik `Siti Nurhaliza`, tekan Enter
22. Klik Name `Siti Nurhaliza` (baris akun sendiri) untuk membuka Detail
23. Hover switch Active header
24. Verifikasi switch Active header tampil namun disabled
25. Verifikasi tooltip switch Active `"You can't manage your own account from here."`
26. Klik menu `[⋯]` header
27. Verifikasi `Edit Profile` tampil dan enabled
28. Verifikasi `Delete User` tampil namun disabled
29. Hover `Delete User`
30. Verifikasi tooltip `Delete User` `"You can't manage your own account from here."`
31. Tekan Esc untuk menutup menu `[⋯]`
32. Hover button `Reset Authenticator`
33. Verifikasi button `Reset Authenticator` tampil namun disabled
34. Verifikasi tooltip `Reset Authenticator` `"Ask another admin to reset your authenticator."`
35. Hover baris Custom Field `Blood Type`
36. Verifikasi icon inline edit Custom Field tampil dan enabled
37. Klik Tab `Role`
38. Hover checkbox Tab Role
39. Verifikasi checkbox Tab Role tampil namun disabled
40. Verifikasi tooltip checkbox Tab Role `"You can't manage your own account from here."`
41. Hover Avatar header
42. Verifikasi `[Edit]` tampil pada Avatar header

### TC-GS-USER-76: Kontrol header dan section target Tier TC untuk aktor Full CRUD

43. Logout, lalu login sebagai Manage user and role (Full CRUD)
44. Buka Global Settings > User > User List (sub-tab Login User)
45. Klik icon Search, ketik `Andi Wijaya`, tekan Enter
46. Klik Name `Andi Wijaya` untuk membuka Detail
47. Hover switch Active header
48. Verifikasi switch Active header tampil namun disabled
49. Verifikasi tooltip switch Active `"You don't have permission to edit."`
50. Klik menu `[⋯]` header
51. Verifikasi `Edit Profile` dan `Delete User` tampil namun disabled
52. Hover `Edit Profile`
53. Verifikasi tooltip `Edit Profile` `"You don't have permission to edit."`
54. Hover `Delete User`
55. Verifikasi tooltip `Delete User` `"You don't have permission to edit."`
56. Tekan Esc untuk menutup menu `[⋯]`
57. Verifikasi sub-section User TAG tampil
58. Verifikasi `Scan TAG`, `Unpair`, dan `Resend Activation/Confirmation Email` Hidden
59. Hover baris Custom Field `Blood Type`
60. Hover icon inline edit Custom Field
61. Verifikasi icon inline edit Custom Field tampil namun disabled
62. Verifikasi tooltip icon inline edit `"You don't have permission to edit."`
63. Klik Tab `Role`
64. Hover checkbox Tab Role
65. Verifikasi checkbox Tab Role tampil namun disabled
66. Verifikasi tooltip checkbox Tab Role `"You don't have permission to edit."`

### TC-GS-USER-77: Kontrol header dan section target Tier RO untuk aktor Full CRUD

67. Klik menu User di sidebar Global Settings
68. Klik icon Search, ketik `Doni Pratama`, tekan Enter
69. Klik Name `Doni Pratama` untuk membuka Detail
70. Hover switch Active header
71. Verifikasi switch Active header tampil namun disabled
72. Verifikasi tooltip switch Active `"You don't have permission to edit."`
73. Klik menu `[⋯]` header
74. Verifikasi `Edit Profile` dan `Delete User` tampil namun disabled
75. Hover `Edit Profile`
76. Verifikasi tooltip `Edit Profile` `"You don't have permission to edit."`
77. Hover `Delete User`
78. Verifikasi tooltip `Delete User` `"You don't have permission to edit."`
79. Tekan Esc untuk menutup menu `[⋯]`
80. Verifikasi sub-section User TAG tampil
81. Verifikasi `Scan TAG` dan `Unpair` Hidden
82. Hover baris Custom Field `Blood Type`
83. Hover icon inline edit Custom Field
84. Verifikasi icon inline edit Custom Field tampil namun disabled
85. Verifikasi tooltip icon inline edit `"You don't have permission to edit."`
86. Klik Tab `Role`
87. Hover checkbox Tab Role
88. Verifikasi checkbox Tab Role tampil namun disabled
89. Verifikasi tooltip checkbox Tab Role `"You don't have permission to edit."`

### TC-GS-USER-78: Kontrol header dan section target Normal untuk aktor Full CRUD

90. Klik menu User di sidebar Global Settings
91. Klik icon Search, ketik `Dewi Lestari`, tekan Enter
92. Klik Name `Dewi Lestari` untuk membuka Detail
93. Verifikasi switch Active header enabled
94. Klik menu `[⋯]` header
95. Verifikasi `Edit Profile` dan `Delete User` enabled
96. Tekan Esc untuk menutup menu `[⋯]`
97. Verifikasi `Scan TAG` enabled
98. Hover baris Custom Field `Blood Type`
99. Verifikasi icon inline edit Custom Field enabled
100. Klik Tab `Role`
101. Verifikasi checkbox Tab Role enabled

### TC-GS-USER-79: Kontrol header dan section target Self untuk aktor Full CRUD

102. Klik menu User di sidebar Global Settings
103. Klik icon Search, ketik `Fajar Nugroho`, tekan Enter
104. Klik Name `Fajar Nugroho` (baris akun sendiri) untuk membuka Detail
105. Hover switch Active header
106. Verifikasi switch Active header tampil namun disabled
107. Verifikasi tooltip switch Active `"You can't manage your own account from here."`
108. Klik menu `[⋯]` header
109. Verifikasi `Edit Profile` tampil dan enabled
110. Verifikasi `Delete User` tampil namun disabled
111. Hover `Delete User`
112. Verifikasi tooltip `Delete User` `"You can't manage your own account from here."`
113. Tekan Esc untuk menutup menu `[⋯]`
114. Hover baris Custom Field `Blood Type`
115. Verifikasi icon inline edit Custom Field tampil dan enabled
116. Klik Tab `Role`
117. Hover checkbox Tab Role
118. Verifikasi checkbox Tab Role tampil namun disabled
119. Verifikasi tooltip checkbox Tab Role `"You can't manage your own account from here."`
120. Hover Avatar header
121. Verifikasi `[Edit]` tampil pada Avatar header dan enabled

### TC-GS-USER-80: Kontrol header dan section target Default User untuk aktor Full CRUD

122. Klik menu User di sidebar Global Settings
123. Klik icon Search, ketik `Hendra Gunawan`, tekan Enter
124. Klik Name `Hendra Gunawan` untuk membuka Detail
125. Hover switch Active header
126. Verifikasi switch Active header tampil namun disabled
127. Verifikasi tooltip switch Active `"Default User cannot be modified."`
128. Klik menu `[⋯]` header
129. Verifikasi `Edit Profile` dan `Delete User` tampil namun disabled
130. Hover `Edit Profile`
131. Verifikasi tooltip `Edit Profile` `"You don't have permission to edit."`
132. Hover `Delete User`
133. Verifikasi tooltip `Delete User` `"Default User cannot be modified."`
134. Tekan Esc untuk menutup menu `[⋯]`
135. Hover baris Custom Field `Blood Type`
136. Hover icon inline edit Custom Field
137. Verifikasi icon inline edit Custom Field tampil namun disabled
138. Verifikasi tooltip icon inline edit `"Default User cannot be modified."`
139. Verifikasi sub-section User TAG tampil
140. Verifikasi `Scan TAG`/`Unpair` Hidden

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (140 langkah) karena ketujuh TC berada di satu kelas harness (Role Matrix visibilitas kontrol, bagian 3a) pada satu layar (User Detail), hanya membaca state dan tidak mengubah data; tiap blok TC membuka Detail targetnya sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Satu langkah `Verifikasi` per klausa Expected (state dan tooltip dipisah, S-01) membuat jumlah langkah besar.
- Urutan TC sumber dipertahankan (TC-GS-USER-74 dan 75 aktor Total Control, TC-GS-USER-76 sampai 80 aktor Full CRUD); tidak ada aksi yang menghapus atau mengubah data.
- Langkah penghubung (aksi tanpa `Verifikasi`): membuka User List dan Search nama target sebelum membuka Detail pada tiap blok (langkah 1 sampai 3 dan awal tiap blok berikutnya), menekan Esc untuk menutup menu `[⋯]`, ganti akun (langkah 43), klik Tab `Role` sebelum membaca checkbox Tab Role (langkah 4 TC menyebut Tab Role sebagai bagian yang diamati), dan hover baris Custom Field sebelum membaca icon inline edit yang muncul saat hover.
- Anchor absence (bagian 8b butir 2): `Verifikasi` "sub-section User TAG tampil" mendahului asersi `Scan TAG`/`Unpair` Hidden pada langkah 57, 80, dan 139; asersi ini tidak ada di TC dan ditambahkan hanya sebagai anchor. `Resend Activation/Confirmation Email` Hidden (TC-GS-USER-76 c) berada pada header Detail yang sama dengan switch Active yang sudah terverifikasi tampil.
- Langkah 5 TC (hover elemen yang disabled) dipenuhi di langkah hover masing-masing elemen sebelum `Verifikasi` tooltip (state sementara diasersi tepat waktu, bagian 8b butir 5).
- Pembagian TC lintas spec: hover Avatar `[Edit]` pada akun sendiri (TC-GS-USER-75 f dan TC-GS-USER-79 e) diverifikasi di spec ini; aksi unggah foto akun sendiri (TC-GS-USER-83) diverifikasi di spec 018.
- Temuan untuk QA:
  - TC-GS-USER-74 c ("Button `Reset Authenticator` (bila Enrolled)") dan TC-GS-USER-75 c tidak menyebut status MFA aktor/target di precondition; spec mensyaratkan Hendra Gunawan (Pre-setup No. 1) dan Siti Nurhaliza berstatus Enrolled.
  - TC-GS-USER-74 d dan TC-GS-USER-75 tidak menyebut kondisi TAG target (`Unpair` hanya relevan bila TAG terpasang, `Scan TAG` bila belum); TC-GS-USER-74 d mengharapkan `Scan TAG`/`Unpair` keduanya tampil dan enabled tanpa precondition TAG; spec mengasersi seperti tertulis.
  - Langkah 4 TC-GS-USER-74 dan TC-GS-USER-80 menyebut Tab Role sebagai bagian yang diamati, tetapi Expected keduanya tidak memuat butir Tab Role; spec tidak mengasersi Tab Role pada kedua TC itu.
  - TC-GS-USER-76 c menyebut `Resend Activation/Confirmation Email` Hidden tanpa menyebut status target (Andi Wijaya) yang membuat Resend relevan; asersi Hidden mengikuti TC.
  - TC-GS-USER-74 e dan TC-GS-USER-75 d menyebut "Icon inline edit Custom Field" tanpa menyebut field mana; spec memakai `Blood Type` (Pre-setup No. 24).
