---
id: TC-GS-USER-E2E-164-tab-role-state-in-flight-optimistic-loading-mini-dan-kontrol-disabled
title: "User Detail Tab Role: State In-flight Checkbox CRUD dan Switch Active (Nilai Langsung Tampil, Indikator Loading Mini, Kontrol Disabled Sesaat, dan Klik Ganda Diabaikan)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-1110
  - TC-GS-USER-1109
coverage:
  web: automated
---

# User Detail Tab Role: State In-flight Checkbox CRUD dan Switch Active (Nilai Langsung Tampil, Indikator Loading Mini, Kontrol Disabled Sesaat, dan Klik Ganda Diabaikan)

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; respons hanya ditahan untuk mengamati state in-flight lalu dilepas sebagai sukses, sehingga bukan kelas harness b).
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login di hook `before` spec ini (akun default suite); halaman dibuka hook `beforeEach` suite; tidak ada ganti akun. Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Dinamis, di-seed lewat API di hook `before` dan dihapus di hook `after`: `Ahmad Fauzi {runId}-164` (padanan Ahmad Fauzi, Tabel Pre-setup No. 13), email `ahmadfauzi+{runId}-164@qwertysystem.net`, Activated, baris `Manage TAG` Active dengan Update tidak tercentang.
- Kebutuhan intercept (`Spectra.intercept()`), dipasang dan dilepas lewat langkah eksplisit; nama endpoint ditentukan tim FE (tidak disebut di TC dan PRD):
  - Respons request update permission checkbox Tab Role (TC-GS-USER-1110): ditahan, lalu dilepas sebagai sukses.
  - Respons request switch Active Tab Role (TC-GS-USER-1109): ditahan, lalu dilepas sebagai sukses.
- Kemampuan teknis (disediakan tim FE/BE): seeding user dengan assignment role lewat API; menghitung request yang terkirim ke endpoint yang di-intercept; membaca indikator loading mini pada switch.
- State global yang diubah: tidak ada. Cleanup di hook `after` (tetap berjalan walau spec gagal di tengah): lepas semua intercept dan hapus user seed.

## Test Steps

### TC-GS-USER-1110: Checkbox CRUD, nilai langsung tampil dan disabled sesaat

1. Klik icon Search, ketik `Ahmad Fauzi {runId}-164`, tekan Enter
2. Klik Name `Ahmad Fauzi {runId}-164` di User List
3. Klik Tab `Role`
4. Pasang intercept pada respons request update permission: tahan respons
5. Centang Update baris `Manage TAG`
6. Verifikasi checkbox Update baris `Manage TAG` langsung tampil tercentang
7. Verifikasi checkbox Update baris `Manage TAG` disabled sesaat selama request berjalan
8. Klik checkbox Update baris `Manage TAG` lagi
9. Verifikasi checkbox Update baris `Manage TAG` tetap tercentang (klik diabaikan)
10. Verifikasi hanya 1 request update permission terkirim
11. Lepaskan respons sukses
12. Verifikasi toast sukses "Success, permissions have been updated."
13. Verifikasi checkbox Update baris `Manage TAG` kembali enabled
14. Verifikasi checkbox Update baris `Manage TAG` tercentang
15. Lepas intercept respons request update permission

### TC-GS-USER-1109: Switch Active, nilai langsung tampil, indikator loading mini, dan kontrol disabled sesaat

16. Pasang intercept pada respons request switch Active: tahan respons
17. Matikan switch Active baris `Manage TAG`
18. Verifikasi switch Active baris `Manage TAG` langsung menampilkan posisi OFF
19. Verifikasi indikator loading mini tampil pada switch Active baris `Manage TAG`
20. Verifikasi switch Active baris `Manage TAG` disabled sesaat
21. Verifikasi checkbox baris `Manage TAG` disabled sesaat
22. Klik switch Active baris `Manage TAG` lagi
23. Verifikasi switch Active baris `Manage TAG` tetap OFF (klik diabaikan)
24. Verifikasi hanya 1 request switch Active terkirim
25. Lepaskan respons sukses
26. Verifikasi toast sukses "Success, role has been updated."
27. Verifikasi indikator loading mini hilang dari switch Active baris `Manage TAG`
28. Verifikasi switch Active baris `Manage TAG` OFF
29. Hover checkbox Update baris `Manage TAG`
30. Verifikasi checkbox Update baris `Manage TAG` tampil namun disabled dengan tooltip `"Turn on this role first."`
31. Lepas intercept respons request switch Active

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Menahan respons hanya untuk mengamati state in-flight (loading, disabled, optimistic) dan bukan kegagalan atau timeout yang dipaksakan, sehingga TC ini bukan kelas harness b (bagian 3 prinsip 13b) dan berada di spec fungsional.
- Urutan TC sumber diubah: TC-GS-USER-1110 mendahului TC-GS-USER-1109 karena TC-GS-USER-1109 mematikan switch `Manage TAG` sehingga checkbox menjadi disabled dan TC-GS-USER-1110 tidak lagi dapat dijalankan pada user seed yang sama.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (Search nama target sebelum Klik Name, R-16), 4 dan 16 (memasang intercept), 11 dan 25 (melepas tahanan), 15 dan 31 (melepas intercept).
- Anchor (bagian 8b butir 11): asersi absence indikator loading (langkah 27) ditulis sesudah langkah 25 (lepas tahanan) dan langkah 26 (toast sukses sebagai anchor bahwa respons sudah diproses).
- Temuan untuk QA:
  - TC-GS-USER-1109 Expected a dan TC-GS-USER-1110 Expected a ("disabled sesaat") tidak menyebut durasi; diasersi selama respons ditahan.
  - TC-GS-USER-1109 Expected b dan TC-GS-USER-1110 Expected b ("klik diabaikan, hanya 1 request terkirim") tidak menyebut cara menghitung request; spec memakai penghitung request yang disediakan tim FE/BE.
  - TC-GS-USER-1109 Expected c menyebut checkbox baris disabled dengan tooltip tanpa menyebut checkbox mana; spec memilih Update.
  - TC-GS-USER-1109 Post Condition ("Baris Manage TAG milik Ahmad Fauzi inactive-retained") tanpa langkah observasi tersendiri; diverifikasi sebagian lewat langkah 28 sampai 30.
  - TC-GS-USER-1109 dan 1110 memakai user Pre-setup (Ahmad Fauzi); spec memakai seed milik spec (S-06).
