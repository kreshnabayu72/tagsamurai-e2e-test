---
id: TC-FA-SU-E2E-411-pohon-group-tanpa-node-disabled-karena-ancestor-atau-descendant-pada-modal-dan-popup
title: "Pohon Group Tanpa Node Disabled karena Ancestor atau Descendant Pemegang Role pada Modal Assign dan Popup Assign Group"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1104
coverage:
  web: automated
---

# Pohon Group Tanpa Node Disabled karena Ancestor atau Descendant Pemegang Role pada Modal Assign dan Popup Assign Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21: Finance & Accounting dengan anak Accounts Payable; Region Jawa dengan anak Jakarta Selatan Distribution Center) dan Transaction Role (Pre-setup #39).
- Kedua pengguna target tanpa Home Group: varian `FaUserNoHG` (Pre-setup #50, Home Group seluruh pengguna dikosongkan) dari `FaUserMain` dan `FaUserOV` sehingga pemilih Group tidak disaring gate Home Group (FI-32, Catatan TC).
- Pengguna target: Mira Anggraini (Disposal × Staff pada Finance & Accounting, descendant Accounts Payable; Pre-setup #39) dan Rina Susanti (Disposal × Monitoring & Report pada Jakarta Selatan Distribution Center, ancestor Region Jawa; 5 penugasan Transaction Role, label `5 roles`; tanpa Global Role dan Group Role; Pre-setup #49 seed `FaUserOV`). Seed `FaUserOV` (Pre-setup #49) wajib disediakan tim FE/BE sebelum eksekusi.
- Rina Susanti juga akun aktor Read Only (Pre-setup #5, `Spectra.env.FA_MURG_RO_PASSWORD`); di spec ini hanya menjadi pengguna target dan tidak dipakai login.
- Data uji: modal Assign dengan Accounts Payable dicentang; popup Assign Group baris Disposal × Staff milik Mira Anggraini; popup Assign Group baris Disposal × Monitoring & Report milik Rina Susanti.
- Kemampuan teknis (disediakan tim FE/BE): seed `FaUserOV` (Pre-setup #49) dan Pre-setup #39. Selektor node pohon, status Disabled, dan tooltip disediakan tim FE.
- State global yang diubah: tidak ada data yang disimpan; modal dibuang lewat `[Leave]` dan popup lewat `[Cancel]`. Suite berjalan serial.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-1104: Pohon Group tidak men-Disabled node yang ancestor atau descendant-nya sudah memegang role: modal Assign dan popup Assign Group

1. Ketik Search `Mira Anggraini`, tekan Enter, lalu klik Name `Mira Anggraini`
2. Klik Tab Role lalu Sub-tab Transaction Role
3. Klik `[+ Assign]`, lalu klik tombol Group
4. Arahkan kursor ke Finance & Accounting
5. Verifikasi Finance & Accounting tampil di pohon, tidak Disabled, dan tanpa tooltip `already assigned`
6. Arahkan kursor ke Accounts Payable
7. Verifikasi Accounts Payable tampil di pohon, tidak Disabled, dan tanpa tooltip `already assigned`
8. Verifikasi Finance & Accounting dan Accounts Payable dapat dicentang
9. Centang Accounts Payable
10. Verifikasi Accounts Payable tercentang (dapat dipilih)
11. Klik `[Select]`
12. Verifikasi tombol Group berlabel `1 Group selected` (Accounts Payable masuk label)
13. Klik `[✕]` pada modal
14. Verifikasi dialog `Unsaved Changes`
15. Klik `[Leave]`
16. Klik `[Assign Group]` pada baris Disposal × Staff
17. Arahkan kursor ke Finance & Accounting
18. Verifikasi Finance & Accounting tampil di pohon, tercentang, dan tanpa tooltip `already assigned`
19. Verifikasi Finance & Accounting dapat dicabut
20. Arahkan kursor ke Accounts Payable
21. Verifikasi Accounts Payable tampil di pohon, tidak Disabled, dan tanpa tooltip `already assigned`
22. Verifikasi Accounts Payable dapat dicentang
23. Verifikasi tidak ada node Disabled karena constraint Home Group pada popup Mira Anggraini (target tanpa Home Group, Pre-setup #50; gate TC-FA-SU-1117)
24. Klik `[Cancel]`
25. Verifikasi popup tertutup dan baris Disposal × Staff Mira Anggraini menampilkan badge Finance & Accounting saja (tidak ada perubahan tersimpan)
26. Buka Settings > User lewat sidebar, ketik Search `Rina Susanti`, tekan Enter, lalu klik Name `Rina Susanti`
27. Klik Tab Role lalu Sub-tab Transaction Role
28. Klik `[Assign Group]` pada baris Disposal × Monitoring & Report
29. Arahkan kursor ke Region Jawa
30. Verifikasi Region Jawa tampil di pohon, tidak Disabled, dan tanpa tooltip `already assigned`
31. Arahkan kursor ke Jakarta Selatan Distribution Center
32. Verifikasi Jakarta Selatan Distribution Center tampil di pohon, tidak Disabled, dan tanpa tooltip `already assigned`
33. Verifikasi tidak ada node Disabled karena constraint Home Group pada popup Rina Susanti (target tanpa Home Group, Pre-setup #50; gate TC-FA-SU-1119)
34. Klik `[Cancel]`
35. Verifikasi popup tertutup dan Sub-tab Transaction Role Rina Susanti tetap memuat lima baris (tidak ada perubahan tersimpan)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 2, 26 dan 27. Search pada langkah 1 dan 26 menemukan baris target (R-16, R-23). Langkah 26 membuka layar secara eksplisit sesudah pindah dari Detail Mira Anggraini ke Detail Rina Susanti (S-14).
- Penutupan modal dirty pada langkah 13 sampai 15 mengikuti S-08; popup Assign Group ditutup lewat `[Cancel]` tanpa dialog (langkah 24, 34).
- Verifikasi status node pada langkah 5, 7, 18, 21, 30 dan 32 satu per node memuat tiga sifat yang dinyatakan TC dalam satu butir Expected: node tidak tersaring (tampil), tidak Disabled, dan tanpa tooltip `already assigned` (elemen "Disabled dengan tooltip" negatif, S-01). Hover mendahului tiap asersi tooltip (bagian 8b butir 5); anchor positif adalah node tampil pada pohon.
- Langkah 35 dan 25 mengamati Expected d "tidak ada perubahan tersimpan" lewat baris Sub-tab yang tetap sama (anchor: Sub-tab tampil). Jumlah lima baris Rina Susanti berasal dari seed `FaUserOV` (Pre-setup #49).
- Temuan untuk QA:
  - Seed #49 `FaUserOV` (Rina Susanti tanpa Global Role dan Group Role, 5 penugasan Transaction Role, label `5 roles`) wajib disediakan tim FE/BE. Rina Susanti juga akun aktor Read Only (Pre-setup #5): spec ini memakainya hanya sebagai target.
  - TC-FA-SU-1104 Expected a menyebut "Accounts Payable ... masuk label tombol Group" tanpa menyebut bentuk labelnya; spec mengasersi label `1 Group selected` dari TC-FA-SU-234.
  - TC-FA-SU-1104 Expected d menyebut "tidak ada ... penyaringan redundansi pada node mana pun" tanpa cara observasi; spec mengasersinya lewat node yang ditinjau tetap tampil di pohon (langkah 5, 7, 18, 21, 30, 32). Mohon dikonfirmasi bila yang dimaksud mencakup node lain.
  - TC-FA-SU-1104 Expected c: Jakarta Selatan Distribution Center tidak Disabled walau sudah tercentang pada baris itu; spec mengasersi tidak Disabled tanpa asersi status centang (TC tidak menyebutnya).
  - TC-FA-SU-1104 Expected d diperbarui (gate Home Group): kedua target tanpa Home Group sehingga tidak ada node Disabled karena constraint; spec menambah satu Verifikasi per target (langkah 23 dan 33) dengan Pre-setup #50. Gabungan seed #49 dan #50 untuk Rina Susanti perlu disediakan tim FE/BE.
  - Preview scope tidak berlaku di TC ini; copy dan selektor tooltip `already assigned` perlu dikonfirmasi tim FE.
