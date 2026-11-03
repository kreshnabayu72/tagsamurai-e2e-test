---
id: TC-FA-FAAM-E2E-202-total-assets-penanda-masa-garansi-strip-time-zone-dan-netral
title: "Tab Total Assets: Penanda Garansi Strip-No access, Time Zone Client, dan Tidak Memengaruhi Sort-Filter-Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-820
  - TC-FA-FAAM-821
  - TC-FA-FAAM-822
coverage:
  web: automated
---

# Tab Total Assets: Penanda Garansi Strip-No access, Time Zone Client, dan Tidak Memengaruhi Sort-Filter-Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Purchase HO (Pre-setup #32c) `managePurchaseHO_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_PHO_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Akun berikutnya (ganti akun eksplisit di `## Test Steps`): Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Akun berikutnya (ganti akun eksplisit di `## Test Steps`): Full Value Access (Pre-setup #32e) `fullValueAccess_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_FVA_PASSWORD`.
- Data: `Warranty Date Item` (Total Asset 6; Pre-setup #36): `AST-3001` hari ini minus 1 hari (`Head Office`), `AST-3002` hari ini, `AST-3003` hari ini plus 30 hari, `AST-3004` hari ini plus 31 hari, `AST-3005` tanpa tanggal garansi (`Head Office`), `AST-3006` hari ini minus 5 hari (`Warehouse`, di luar hak Purchase HO); tanggal disemai relatif terhadap tanggal hari berjalan. Client `AutoTimeZone` (Pre-setup #36b): `Time Zone Item` (Total Asset 1, aset `AST-3101`, Warranty Expiry sama dengan tanggal hari ini menurut Time Zone `Pacific/Pago_Pago`); akun Total Control pada client ini disediakan tim FE.
- State global: Time Zone General Settings client `AutoTimeZone` diubah ke `Pacific/Pago_Pago` lalu `Pacific/Kiritimati` pada blok TC-FA-FAAM-821; hook `after` memulihkan Time Zone ke nilai awal (kemampuan disediakan tim FE/BE). Suite berjalan serial (`parallel: false`).
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- Preferensi Setup Column tersimpan per akun (keputusan pemilik 2026-11-02), jadi centang kolom akun sebelumnya tidak terbawa ke akun berikutnya.
- Kemampuan teknis: pembacaan berkas CSV yang terunduh (nama berkas, header, dan isi sel) disediakan tim FE.

## Test Steps

### TC-FA-FAAM-820: Sel strip dan No access tidak diberi penanda warna

1. Klik nama `Warranty Date Item`, klik tab `Total Assets (6)`
2. Klik header Actions (⋯), pilih `Setup Column...`, centang Warranty Expiry, klik `[Save]`
3. Verifikasi `AST-3001` menampilkan penanda kelas danger (pembanding)
4. Verifikasi `AST-3005` menampilkan `—` tanpa penanda warna
5. Verifikasi `AST-3006` menampilkan `No access` tanpa penanda danger maupun warning
6. Hover sel `AST-3006`
7. Verifikasi tooltip `Requires Manage purchase access in this group.`
8. Tutup popup Detail, klik tombol akun, pilih Logout

### TC-FA-FAAM-821: Penanda masa garansi memakai Time Zone General Settings client untuk menentukan hari ini

9. Login sebagai Total Control pada client `AutoTimeZone` (`totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`)
10. Ubah Time Zone di General Settings menjadi `Pacific/Pago_Pago`, buka Fixed Asset > Settings > Asset Master > Asset Name, klik nama `Time Zone Item`, klik tab `Total Assets (1)`
11. Klik header Actions (⋯), pilih `Setup Column...`, centang Warranty Expiry, klik `[Save]`
12. Verifikasi Time Zone `Pacific/Pago_Pago`: sel `AST-3101` menampilkan penanda kelas warning
13. Verifikasi Time Zone `Pacific/Pago_Pago`: hover menampilkan tooltip `Warranty expires soon`
14. Tutup popup Detail, ubah Time Zone di General Settings menjadi `Pacific/Kiritimati`, buka Fixed Asset > Settings > Asset Master > Asset Name, klik nama `Time Zone Item`, klik tab `Total Assets (1)`
15. Verifikasi Time Zone `Pacific/Kiritimati`: sel `AST-3101` menampilkan penanda kelas danger
16. Verifikasi Time Zone `Pacific/Kiritimati`: hover menampilkan tooltip `Warranty expired`
17. Tutup popup Detail, klik tombol akun, pilih Logout

### TC-FA-FAAM-822: Penanda masa garansi tidak memengaruhi Sort, Filter, Search, dan Download

18. Login sebagai Full Value Access (`fullValueAccess_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_FVA_PASSWORD`)
19. Buka Fixed Asset > Settings > Asset Master > Asset Name, klik nama `Warranty Date Item`, klik tab `Total Assets (6)`
20. Klik header Actions (⋯), pilih `Setup Column...`, centang Warranty Expiry, klik `[Save]`
21. Klik header Warranty Expiry 1 kali
22. Verifikasi Sort `Oldest First`: `AST-3006`, `AST-3001`, `AST-3002`, `AST-3003`, `AST-3004`, lalu `AST-3005` (`—`) di akhir; urutan hanya menurut tanggal
23. Klik header Warranty Expiry 2 kali lagi sampai kembali ke default
24. Klik Filter, pilih Warranty Expiry rentang hari ini minus 1 hari sampai hari ini, klik `[Apply]`
25. Verifikasi Filter hari ini minus 1 hari sampai hari ini: hanya `AST-3001` dan `AST-3002` tampil
26. Klik Filter, klik `[Clear Field]`, klik `[Apply]` (menghapus filter)
27. Ketik Search teks tanggal Warranty Expiry `AST-3001` sebagaimana tampil, tekan Enter
28. Verifikasi Search teks tanggal tidak menemukan baris (kolom tidak Searchable)
29. Klik `(←)` pada kotak Search
30. Klik Download lalu `Download as CSV`
31. Verifikasi berkas CSV terunduh
32. Verifikasi berkas memuat tanggal asli dalam format General Settings tanpa warna dan tanpa teks tooltip
33. Verifikasi `AST-3005` pada berkas ditulis hyphen tunggal `-`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 820 (Purchase HO), 821 (Total Control pada client `AutoTimeZone`), 822 (Full Value Access); ganti akun dan ganti client punya langkah eksplisit (S-07). Ketiga bagian tetap bermakna walau bagian sebelumnya gagal.
- Langkah penghubung: `(←)` pada Search, `[Clear Field]` dan `[Apply]` untuk menghapus filter, serta menutup popup Detail dan Logout sebelum ganti akun atau client.
- Time Zone General Settings diubah pada blok TC-FA-FAAM-821 dan dipulihkan oleh hook `after` (R-08).
- TC-FA-FAAM-822 memuat asersi isi berkas CSV (kelas f) dalam TC fungsional yang sama; spec mengikuti TC.
- Temuan untuk QA:
  - TC-FA-FAAM-821: email akun Total Control pada client `AutoTimeZone` tidak tertulis di Pre-setup #36b; spec memakai akun Total Control yang disediakan tim FE.
  - TC-FA-FAAM-822 langkah 5 ("Klik header 2 kali dan 1 kali lagi hingga default") dituliskan sebagai dua klik tambahan sampai kembali ke default.
