---
id: TC-FA-SU-E2E-151-sub-tab-assigned-assets-search
title: "Sub-tab Assigned Assets: Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-446
  - TC-FA-SU-447
coverage:
  web: automated
---

# Sub-tab Assigned Assets: Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook suite dinyatakan di `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup (hanya dibaca, tidak diubah): Client `FaUserMain` (#20) dan Responsibilities (#24): Detail Budi Santoso dengan Sub-tab Assigned Assets 5 baris (satu halaman). Nilai dibaca dari `Fixture.faSettingsUser.preSetup` (fixture belum ada, disediakan tim FE). Pre-setup #24 hanya menyebut "5 baris"; nilai kolom di bawah diturunkan dari Expected TC (Asset ID dan Transaction ID hanya tertulis sebagian):

| Name | Asset ID | Transaction ID | Brand | Model / Type | PIC |
|---|---|---|---|---|---|
| `AC Split Ruang Kerja` | tidak tertulis | tidak tertulis | `Daikin` | `1PK` | `Ahmad D` |
| `Lemari Arsip` | tidak tertulis | tidak tertulis | `Lion` | `2 Pintu` | `Citra L` |
| `Meja Kerja Kepala Divisi` | tidak tertulis | `ASG-20260505` | `Modera` | `Executive` | `Ahmad D` |
| `Printer Multifungsi` | tidak tertulis | tidak tertulis | `Canon` | `PIXMA G3010` | `Citra L` |
| `Server Rack Mini` | `AST-02113` | tidak tertulis | `HP` | `ProLiant DL20` | `Eka W` (Eka Wulandari) |
- Data Dinamis: tidak ada.
- State global: tidak ada yang diubah; spec hanya membaca Pre-setup. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-446: Siklus interaksi Search Sub-tab Assigned Assets: reveal, Enter, clear, collapse

1. Klik nama `Budi Santoso` di User List
2. Klik tab Responsibilities, lalu klik Sub-tab Assigned Assets
3. Klik icon Search
4. Verifikasi input Search melebar
5. Verifikasi kursor fokus di input Search
6. Verifikasi placeholder Search `Search name, asset ID, or transaction ID...`
7. Hover icon Search
8. Verifikasi tooltip `Search` tampil
9. Ketik satu karakter `P` pada input Search
10. Verifikasi icon ✕ tampil di kanan input
11. Verifikasi tabel belum tersaring dan menampilkan sedikitnya satu baris
12. Ketik sisa `rinter` pada input Search, tekan Enter
13. Verifikasi tabel tersaring menjadi `Printer Multifungsi`
14. Klik ✕
15. Verifikasi input Search kosong
16. Verifikasi search bar tetap terbuka
17. Verifikasi kursor fokus di input Search
18. Verifikasi tabel tetap menampilkan hasil search terakhir `Printer Multifungsi`
19. Tekan Enter
20. Verifikasi tabel kembali menampilkan semua baris
21. Ketik Search `Printer`, tekan Enter
22. Klik `(←)` pada kotak Search
23. Verifikasi search bar menutup
24. Verifikasi tabel langsung kembali menampilkan semua baris
25. Klik icon Search
26. Verifikasi keyword pada input Search dikosongkan
27. Ketik Search `  Printer  `, tekan Enter
28. Verifikasi hasil sama dengan `Printer` tanpa spasi, yaitu `Printer Multifungsi`
29. Verifikasi isi input Search tetap `  Printer  `

### TC-FA-SU-447: Search Sub-tab Assigned Assets terikat visibilitas kolom Name: hide lalu unhide

30. Ganti isi kotak search dengan `Printer`, tekan Enter
31. Verifikasi keyword `Printer` menyisakan `Printer Multifungsi`
32. Klik header Actions (⋯)
33. Uncheck kolom Name pada overlay Column Visibility
34. Ganti isi kotak search dengan `Printer`, tekan Enter
35. Verifikasi tabel tidak menampilkan baris
36. Klik header Actions (⋯)
37. Check kolom Name pada overlay Column Visibility
38. Ganti isi kotak search dengan `Printer`, tekan Enter
39. Verifikasi keyword `Printer` menyisakan `Printer Multifungsi`
40. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pembukaan Detail dan sub-tab (langkah 1 dan 2) serta langkah yang mengosongkan Search, Filter, atau popup di antara blok TC supaya blok berikutnya tidak mengandalkan state blok sebelumnya (S-09).
- Search hanya menyaring saat Enter (bagian 8b butir 9). Blok TC-FA-SU-447 memakai kotak Search yang masih terbuka dari TC-FA-SU-446 ("ganti isi kotak search"); input diisi ulang tiap kali visibilitas kolom berubah supaya penyaringan dijalankan ulang.
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (40 langkah, 40 langkah nominal). Seluruhnya satu kelas (fungsional/screening sub-tab Assigned Assets, satu akun, data Pre-setup sama, tanpa mengubah data Pre-setup), dan tiap blok TC berdiri sendiri: kegagalan satu blok tidak menghilangkan makna blok lain. Satu pembukaan Detail dipakai bersama seluruh blok.
- Pembagian TC lintas spec: TC-FA-SU-442 sampai 445 ada di spec 150.
- Temuan untuk QA (S-15):
  - TC-FA-SU-446 Expected b menyebut tabel "belum tersaring" tanpa menyebut jumlah baris; spec mengasersi lima baris Pre-setup tampil.
  - TC-FA-SU-446 Expected f ("keyword dikosongkan" setelah collapse) tidak teramati saat search bar tertutup; spec mengasersinya dengan membuka kembali icon Search dan memeriksa input kosong.
