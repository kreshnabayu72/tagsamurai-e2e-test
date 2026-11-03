---
id: TC-FA-LIC-E2E-092-group-license-allocation-setup-column-reset-x-esc-satu
title: "Group License Allocation: Setup Column Satu Kolom Tersisa, X atau Esc, Reset to Default, dan Guard Tabel Summary"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-320
  - TC-FA-LIC-321
  - TC-FA-LIC-322
  - TC-FA-LIC-363
coverage:
  web: automated
---

# Group License Allocation: Setup Column Satu Kolom Tersisa, X atau Esc, Reset to Default, dan Guard Tabel Summary

## Prerequisites

- Mode: FE+BE (backend nyata, tanpa mock).
- Akun: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Data Pre-setup #12 (data kuota dan hierarki PT Sejahtera, dipulihkan fixture BE di hook `before`): client Paid Pre-setup #1 dengan `License allocation per group` ON; hierarki Produksi, Kantor Pusat (Divisi Logistik, Divisi IT, Divisi Keuangan), Cabang Surabaya, Cabang Medan. Tabel Group License Allocation pada node All Groups menampilkan empat baris level 1 dengan 13 kolom data tampil: `Group Name`, `Group Code`, `Allocated Quota`, `Allocated to Subgroups`, `Used by This Group`, `Reserved by This Group`, `Remaining Quota`, `+ Audit`, `+ Tracking`, `+ Maintenance Routine`, `+ Repair Ticketing`, `+ Maps`, `+ IT Inventory`. Identitas dan nilai data dirujuk lewat `Fixture.fixedAssetLicense.kuotaHierarki` (belum ada, disiapkan tim FE).
- Data Dinamis: tidak ada.
- Konfigurasi kolom: spec ini menyimpan Setup Column di browser. Konfigurasi dikembalikan ke susunan default oleh langkah `[Reset to Default]` dan `[Save]`, dan hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (dinyatakan di `suite.md`; kemampuan disediakan tim FE).
- Hook dan kemampuan suite (dinyatakan sekali di `suite.md`): fixture BE pemulih Pre-setup #12; pemulihan konfigurasi kolom. Kemampuan teknis: seret-dan-lepas item daftar kolom, mengirim tombol `Esc`, membaca tooltip checkbox disabled, membaca lebar dan perataan kolom tabel.

## Test Steps

### TC-FA-LIC-322: Satu kolom visible tersisa tidak dapat di-uncheck

1. Klik tab Allocation Quota di node All Groups
2. Buka Popup Setup Column lewat header kolom Actions `⋯` lalu `Setup Column...`
3. Hilangkan centang semua kolom kecuali `Group Name`
4. Coba hilangkan centang kolom terakhir `Group Name`
5. Verifikasi checkbox kolom terakhir disabled
6. Arahkan kursor ke checkbox itu
7. Verifikasi tooltip `At least one column must remain visible.`
8. Klik `(×)` untuk menutup popup tanpa menyimpan

### TC-FA-LIC-321: X atau Esc membuang perubahan

9. Buka Popup Setup Column, hilangkan centang `Group Code`
10. Klik `(×)`
11. Verifikasi popup tertutup
12. Verifikasi tabel memakai konfigurasi tersimpan terakhir: kolom `Group Code` masih tampil
13. Buka Popup Setup Column, hilangkan centang `Group Code`
14. Tekan `Esc`
15. Verifikasi popup tertutup
16. Verifikasi perubahan preview dibuang dan tabel memakai konfigurasi tersimpan terakhir: kolom `Group Code` masih tampil

### TC-FA-LIC-320: Reset to Default

17. Buka Popup Setup Column, hilangkan centang `Group Code`, dan seret `+ IT Inventory` ke posisi pertama
18. Klik `[Reset to Default]`
19. Verifikasi Live Preview kembali ke susunan default modul: `Group Name`, `Group Code`, `Allocated Quota`, `Allocated to Subgroups`, `Used by This Group`, `Reserved by This Group`, `Remaining Quota`, `+ Audit`, `+ Tracking`, `+ Maintenance Routine`, `+ Repair Ticketing`, `+ Maps`, `+ IT Inventory`
20. Klik `[Save]`
21. Verifikasi susunan default tersimpan pada tabel
22. Muat ulang halaman (F5)
23. Verifikasi susunan default bertahan setelah F5

### TC-FA-LIC-363: Guard License Summary dan Group Quota Summary, tanpa TableTools dan paginator, kolom Actions kosong

24. Klik node `Kantor Pusat` pada Sidebar
25. Verifikasi tabel License Summary dan tabel Group Quota Summary read-only tanpa Search, Filter, TableTools, dan paginator (Sort, Search, dan Filter tidak berlaku)
26. Verifikasi header kolom Actions `⋯` tampil pada tabel License Summary sebagai pemicu Column Visibility dan `Setup Column...`
27. Verifikasi header kolom Actions `⋯` tampil pada tabel Group Quota Summary sebagai pemicu Column Visibility dan `Setup Column...`
28. Verifikasi sel kolom Actions pada kedua tabel kosong (tanpa tombol aksi)
29. Verifikasi lebar kolom `License` pada tabel License Summary 160px rata kiri
30. Verifikasi kolom angka pada tabel License Summary rata kanan

## Notes

- Langkah penghubung tanpa `Verifikasi`: menutup popup dengan `(×)` pada TC-FA-LIC-322 (S-09) dan membuka node `Kantor Pusat` pada TC-FA-LIC-363. Setup Column tidak memakai "Tunggu aksi selesai" karena aksi sisi klien (butir 8 bagian 8b).
- TC-FA-LIC-321 menyebut "klik `(×)` atau tekan Esc" tanpa menyebut salah satu; spec menjalankan keduanya berurutan sebagai dua varian.
- TC-FA-LIC-363 ada di spec ini bersama TC Setup Column karena memeriksa header kolom Actions `⋯` sebagai pemicu Column Visibility dan Setup Column pada tabel Summary.
- Temuan untuk QA: TC-FA-LIC-320 langkah 2 ("ubah visibilitas dan urutan beberapa kolom") tidak menyebut kolom yang diubah; spec memakai menyembunyikan `Group Code` dan menyeret `+ IT Inventory` ke posisi pertama.
