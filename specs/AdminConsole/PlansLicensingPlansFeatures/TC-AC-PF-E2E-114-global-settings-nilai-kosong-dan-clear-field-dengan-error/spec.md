---
id: TC-AC-PF-E2E-114-global-settings-nilai-kosong-dan-clear-field-dengan-error
title: "Global Settings: Nilai Kosong Ditolak dan Clear Field Menghapus Pesan Error"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-637
  - TC-AC-PF-638
  - TC-AC-PF-662
coverage:
  web: automated
---

# Global Settings: Nilai Kosong Ditolak dan Clear Field Menghapus Pesan Error

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active).
- Data: Global FAMS Settings tersimpan `Max custom fields per asset name` = `5` dan `Max depreciation methods (Multi Depreciation tier)` = `2` (precondition TC; Tabel Pre-setup tidak memuat baris bernomor untuk data ini, lihat Temuan untuk QA). General Settings baseline (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- State global: suite serial (`parallel: false`). Global FAMS Settings adalah singleton dan tidak dapat dimiliki spec (S-06, pengecualian 2026-10-30): nilai `5` dan `2` dipulihkan lewat Fixture BE (idempoten, disediakan tim FE/BE) di hook `before` dan `after`. Spec ini tidak menyimpan perubahan apa pun (semua Save ditolak validasi), sehingga tidak ada entri Changelog baru.
- Baseline Changelog Global Settings: jumlah entri (N) dibaca lewat kemampuan baca di hook `before` (audit trail permanen, N tidak dapat diturunkan dari seeding; S-12, bagian 8b butir 10). Karena spec ini tidak menambah entri, N tetap sama sepanjang spec.
- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca jumlah entri Changelog Global Settings; dialog `beforeunload` bawaan browser pada F5 dapat dikonfirmasi oleh spec (S-08).
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.

## Test Steps

### TC-AC-PF-637: Max custom fields per asset name kosong

1. Klik tab `Global Settings`
2. Hapus seluruh isi input `Max custom fields per asset name`
3. Verifikasi Tidak ada pesan error di bawah input `Max custom fields per asset name` sebelum Save
4. Klik `[Save]`
5. Verifikasi Pesan inline `Max custom fields per asset name must not be empty` tampil di bawah input
6. Verifikasi Tidak ada toast sukses
7. Verifikasi Input `Max depreciation methods (Multi Depreciation tier)` tetap `2`
8. Verifikasi Input `Max depreciation methods (Multi Depreciation tier)` tanpa pesan error
9. Tekan F5 dan konfirmasi dialog `beforeunload` karena form dirty
10. Verifikasi Nilai tersimpan `Max custom fields per asset name` tetap `5`
11. Klik ikon Changelog di Card tab Global Settings
12. Verifikasi Modal Changelog Global Settings tampil dengan entri sebelumnya (anchor)
13. Verifikasi Jumlah entri Changelog Global Settings sama dengan baseline N (tidak ada entri baru)
14. Tutup modal Changelog

### TC-AC-PF-638: Max depreciation methods (Multi Depreciation tier) kosong

15. Hapus seluruh isi input `Max depreciation methods (Multi Depreciation tier)`
16. Verifikasi Tidak ada pesan error di bawah input `Max depreciation methods (Multi Depreciation tier)` sebelum Save
17. Klik `[Save]`
18. Verifikasi Pesan inline `Max depreciation methods (Multi Depreciation tier) must not be empty` tampil di bawah input
19. Verifikasi Tidak ada toast sukses
20. Verifikasi Input `Max custom fields per asset name` tetap `5`
21. Verifikasi Input `Max custom fields per asset name` tanpa pesan error
22. Tekan F5 dan konfirmasi dialog `beforeunload` karena form dirty
23. Verifikasi Nilai tersimpan `Max depreciation methods (Multi Depreciation tier)` tetap `2`
24. Klik ikon Changelog di Card tab Global Settings
25. Verifikasi Modal Changelog Global Settings tampil dengan entri sebelumnya (anchor)
26. Verifikasi Jumlah entri Changelog Global Settings sama dengan baseline N (tidak ada entri baru)
27. Tutup modal Changelog

### TC-AC-PF-662: Clear Field menghapus pesan error inline dan memindahkan fokus

28. Kosongkan `Max custom fields per asset name`, lalu klik `[Save]`
29. Verifikasi Pesan `Max custom fields per asset name must not be empty` tampil
30. Klik `[Clear Field]`
31. Verifikasi Pesan `Max custom fields per asset name must not be empty` hilang
32. Verifikasi `Max custom fields per asset name` kembali bernilai `5`
33. Verifikasi `Max depreciation methods (Multi Depreciation tier)` kembali bernilai `2`
34. Verifikasi Fokus berada pada `Max custom fields per asset name`
35. Verifikasi Tidak ada dialog konfirmasi
36. Verifikasi Form tetap terbuka

## Notes

- Langkah penghubung (S-03): klik tab `Global Settings` sebagai precondition TC-AC-PF-637 (langkah 1). Langkah 29 (Verifikasi pesan error tampil) bukan butir Expected TC-AC-PF-662; langkah itu hanya menjadi anchor positif bagi asersi "pesan hilang" pada langkah 31 (bagian 8b butir 2).
- Asersi "tidak ada entri Changelog baru" (TC-AC-PF-637 dan TC-AC-PF-638 butir d) ditulis sebagai asersi jumlah terhadap baseline N (S-12), didahului anchor positif; bukan spec absence. Spec absence TC-AC-PF-538 ada di spec 125 dan tidak memuat kedua TC ini.
- Alasan melewati sekitar 35 langkah (36 langkah): ketiga blok memakai satu halaman, dua input yang sama, dan satu kelas harness (fungsional). Tambahan langkah berasal dari S-01 yang memecah Expected bermajemuk TC-AC-PF-637 dan TC-AC-PF-638 (masing-masing empat butir, delapan klausa). Blok baca-log (langkah 11 sampai 14 dan 24 sampai 27) mengikuti pola buka surface lalu Verifikasi, yang tidak dihitung pada ambang menurut bagian 3 prinsip 13.
- Temuan untuk QA:
  - Tabel Pre-setup TC tidak memuat baris bernomor untuk nilai awal Global FAMS Settings (`5` dan `2`); nilai itu hanya tertulis di precondition tiap TC. Spec memakai S-06 pengecualian 2026-10-30 (singleton, pemulihan lewat Fixture BE).
  - TC-AC-PF-637 dan TC-AC-PF-638 langkah 4 ("Muat ulang halaman") ditulis dengan penanganan dialog `beforeunload` karena form masih dirty (field kosong); TC tidak menyebut dialog itu.
  - TC-AC-PF-662 langkah 1 meminta "amati pesan error" tetapi Expected tidak memuat butir pesan error tampil; spec menambah langkah 29 sebagai anchor (lihat catatan S-03 di atas).
