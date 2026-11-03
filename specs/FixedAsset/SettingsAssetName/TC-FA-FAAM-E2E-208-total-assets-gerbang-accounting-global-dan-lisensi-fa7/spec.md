---
id: TC-FA-FAAM-E2E-208-total-assets-gerbang-accounting-global-dan-lisensi-fa7
title: "Tab Total Assets Gerbang Akses: Aktor Accounting Global dan Lisensi FA-7 Grace Period atau Tidak Aktif"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-785
  - TC-FA-FAAM-806
  - TC-FA-FAAM-807
coverage:
  web: automated
---

# Tab Total Assets Gerbang Akses: Aktor Accounting Global dan Lisensi FA-7 Grace Period atau Tidak Aktif

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Accounting Global (Pre-setup #32b) `manageAccounting_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_ACCG_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Akun berikutnya (ganti akun eksplisit di `## Test Steps`): Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Data: `Column Matrix Item` (Code `CMX`, Category `Laptop` anak `Electronics`, Brand `Dell` model `5420`, UoM `Kilogram` Symbol `kg`, Total Asset 6; Pre-setup #33, #33b, #33c, #33d, #33e). Enam aset berstatus `Active`, Last Updated menurun dari `AST-2001` (20 Oct 2026 10:00) sampai `AST-2006` (15 Oct 2026): `AST-2001` Group `Head Office`, tag aktif `QR` (Tag Code `TGC-2001`) dan `RFID`, Asset Value (Commercial) 15000000, Warranty Expiry 31 Mar 2027, Last Scanned 10 Oct 2026 09:00; `AST-2002` `Head Office`, tag `QR`, Asset Value 0, tanpa Warranty, belum dipindai; `AST-2003` `Finance` (anak `Head Office`), tanpa tag aktif, tanpa Asset Value, Warranty 15 Jan 2026, Last Scanned 05 Oct 2026 14:30; `AST-2004` `Warehouse`, tag `RFID`, Asset Value 5000000, Warranty 30 Jun 2028, belum dipindai; `AST-2005` `Warehouse`, tag `NFC` dan `QR`, Asset Value 20000000, Warranty 01 Feb 2025, Last Scanned 12 Sep 2026 08:15; `AST-2006` `Warehouse`, tag `NFC`, tanpa Asset Value, tanpa Warranty, belum dipindai. `Accounting Code` (Text, Accounting; `ACC-1` `AST-2001`, `ACC-4` `AST-2004`), lisensi `FA-7` aktif pada client utama (Pre-setup #33e). Accounting Global memegang Global Role `Manage accounting` (tanpa Group Role); Purchase tidak dimiliki.
- Client salinan (Pre-setup #35, #35b): `AutoFA7Grace` (lisensi `FA-7` berstatus Grace Period) dan `AutoFA7Off` (lisensi `FA-7` tidak aktif, bukan Grace Period), masing-masing berisi salinan `Column Matrix Item` dan custom field `Accounting Code` (Text, Accounting; `ACC-1` `AST-2001`). Akun Total Control pada kedua client disediakan tim FE (lihat Temuan untuk QA).
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- Preferensi Setup Column tersimpan per akun (keputusan pemilik 2026-11-02), jadi centang kolom akun sebelumnya tidak terbawa ke akun berikutnya.
- Kemampuan teknis (TC-FA-FAAM-807): pengamatan respons jaringan data Tab Total Assets dan klien HTTP bersesi aktor yang sama untuk request langsung ke endpoint data Tab Total Assets; endpoint tidak disebut TC, PRD, atau LLD dan disediakan tim BE/FE (S-13).
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-785: Gerbang akses sel: aktor Manage accounting global (Asset Value seluruh baris, Accounting terbuka, Warranty No access)

1. Klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
2. Klik header Actions (⋯), pilih `Setup Column...`, amati kolom yang tersedia
3. Verifikasi Setup Column memuat `Asset Value`, `Warranty Expiry`, dan `Accounting Code`
4. Verifikasi Setup Column tidak memuat `Purchase Price`
5. Centang Asset Value, Warranty Expiry, dan `Accounting Code` (kolom `Purchase Price` tidak tersedia pada daftar), klik `[Save]`
6. Verifikasi Asset Value: `AST-2001` 15000000, `AST-2002` currency nol (mis. `Rp 0,00`), `AST-2003` `—`, `AST-2004` 5000000, `AST-2005` 20000000, `AST-2006` `—`
7. Verifikasi Asset Value: tidak ada `No access` (hak client-wide)
8. Verifikasi Warranty Expiry: keenam baris `No access` (aktor tidak memegang Manage purchase)
9. Verifikasi Accounting Code: `AST-2001` `ACC-1`, `AST-2004` `ACC-4`, baris lain `—`
10. Verifikasi Accounting Code: tidak ada `No access`
11. Verifikasi sel kolom Name, Asset ID, Brand, Group, Status tetap tampil normal pada keenam baris
12. Tutup popup Detail, klik tombol akun, pilih Logout

### TC-FA-FAAM-806: Kolom Accounting tersedia read-only saat lisensi FA-7 berstatus Grace Period

13. Login sebagai Total Control pada client `AutoFA7Grace` (`totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`), buka Fixed Asset > Settings > Asset Master > Asset Name
14. Klik nama `Column Matrix Item`, klik tab `Total Assets (6)`, klik header Actions (⋯), pilih `Setup Column...`, amati kolom `Accounting Code`
15. Verifikasi Setup Column memuat `Accounting Code`
16. Centang `Accounting Code`, klik `[Save]`
17. Verifikasi kolom `Accounting Code` tampil dan `AST-2001` menampilkan `ACC-1`
18. Verifikasi tab tidak menyediakan aksi tulis pada nilai kolom (read-only)
19. Tutup popup Detail, klik tombol akun, pilih Logout

### TC-FA-FAAM-807: Kolom Accounting tidak tersedia dan nilainya tidak dikembalikan server saat lisensi FA-7 tidak aktif

20. Login sebagai Total Control pada client `AutoFA7Off` (`totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`), buka Fixed Asset > Settings > Asset Master > Asset Name
21. Klik nama `Column Matrix Item` dengan pemantauan respons jaringan, klik tab `Total Assets (6)`, klik header Actions (⋯), pilih `Setup Column...`, amati kolom `Accounting Code`
22. Verifikasi Setup Column memuat kolom lain (mis. `Asset Value`) dan tidak memuat `Accounting Code`
23. Periksa payload respons data tab untuk keenam baris
24. Verifikasi payload respons tidak memuat nilai `Accounting Code` (`ACC-1`) untuk aset mana pun
25. Kirim request langsung ke endpoint data Tab Total Assets memakai sesi yang sama
26. Verifikasi payload respons request langsung tidak memuat nilai `Accounting Code` (`ACC-1`) untuk aset mana pun

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- K-1: TC-FA-FAAM-807 adalah TC defense-in-depth dengan Expected respons API (payload respons data tab dan request langsung ke server) yang tetap masuk spec FE+BE; asersi request langsung hanya respons server (bagian 8b butir 1).
- Urutan TC: 785 (Accounting Global, client utama), lalu ganti akun dan client ke Total Control pada `AutoFA7Grace` untuk 806, lalu `AutoFA7Off` untuk 807 (S-07: ganti akun dan ganti client punya langkah eksplisit). Ketiga bagian tetap bermakna walau bagian sebelumnya gagal.
- Langkah penghubung: menutup popup Detail dan Logout sebelum ganti akun atau client.
- Temuan untuk QA:
  - Pre-setup #35 dan #35b tidak mencantumkan email akun Total Control pada client `AutoFA7Grace` dan `AutoFA7Off`; spec memakai akun Total Control yang disediakan tim FE.
  - TC-FA-FAAM-806 butir c ("Tab tidak menyediakan aksi tulis pada nilai kolom") tidak menyebut elemen aksi tulis yang dicek; spec mengasersi tidak ada aksi tulis pada kolom Accounting Code.
  - TC-FA-FAAM-785 LK langkah 4 bersyarat ("bila tersedia"); spec menulis centang hanya pada kolom yang terbukti tersedia lewat Expected a.
