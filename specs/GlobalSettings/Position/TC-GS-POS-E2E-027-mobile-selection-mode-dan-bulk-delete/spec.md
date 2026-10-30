---
id: TC-GS-POS-E2E-027-mobile-selection-mode-dan-bulk-delete
title: "Mobile Android: Aturan Card dan Menu, Screening Toolbar, dan Selection Mode Long-press untuk Bulk Delete Position"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-151
  - TC-GS-POS-298
  - TC-GS-POS-304
coverage:
  mobile: automated
---

# Mobile Android: Aturan Card dan Menu, Screening Toolbar, dan Selection Mode Long-press untuk Bulk Delete Position

## Prerequisites

- Mode: FE+BE (aplikasi Android terhadap backend nyata).
- Platform: aplikasi Android TAG Samurai Mobile (`coverage.mobile`); spec tidak berjalan di web. Perangkat atau emulator Android dengan gesture long-press, tap, dan bottom sheet. Spec ini memakai perangkat bersama: `parallel: false` (Suite serial).
- Akun aktor pertama: Manage user and role Read-Only `manageUserRoleRead_automated_{namaCompany}@qwertysystem.net` (Pre-setup 4), `Spectra.env.GS_READ_PASSWORD`. Login di hook `before` pada aplikasi Android. Layar awal: hook `beforeEach` membuka User > Position di aplikasi Android; spec tidak menguji navigasi sehingga tidak mengulang langkah buka di `## Test Steps` (kecuali sesudah ganti akun, langkah 12).
- Akun aktor kedua (ganti akun eksplisit pada langkah 12): Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1), `Spectra.env.GS_TC_PASSWORD`. Akun ini akun default suite sehingga hook `after` tidak perlu memulihkan sesi. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (tetap di environment, tidak diubah spec ini, tanpa suffix): Position 10-16 (7 record) memenuhi precondition "≥2 record" untuk TC-GS-POS-298 dan 304.
- Data Dinamis (di-seed lewat API di hook `before`; bebas relasi dan tidak dipakai user; nama bersuffix per run; fixture baru `Fixture.position.mobileBulkSeed027`): `Account Executive {runId}-027` dan `Business Analyst {runId}-027`. Keduanya dihapus oleh TC-GS-POS-151.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua Position bersuffix `{runId}-027` yang masih ada.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` menjadi true untuk akun aktor spec ini (kedua akun) dan hook `after` memulihkannya (lihat `suite.md`).
- Environment variable: `GS_READ_PASSWORD`, `GS_TC_PASSWORD`.
- Tidak ada state global lain yang diubah.

## Test Steps

### TC-GS-POS-298: Mobile, aturan kolom dan menu card yang berbeda dari web (akun Read-Only)

1. Verifikasi card hanya menampilkan Name
2. Verifikasi `[⋯]` row action tidak tampil pada card (Edit dan Delete Hidden untuk aktor ini)
3. Tap `[⋯]` toolbar
4. Buka Column Visibility
5. Verifikasi Column Visibility memuat `Name`
6. Verifikasi Column Visibility tidak memuat `Last Updated`
7. Tutup bottom sheet Column Visibility
8. Buka opsi sort yang tersedia
9. Verifikasi opsi sort memuat `Name`
10. Verifikasi opsi sort tidak memuat `Last Updated`
11. Tutup opsi sort

### Ganti akun

12. Keluar dari akun Read-Only lalu login sebagai Total Control dengan `Spectra.env.GS_TC_PASSWORD`, kemudian buka User > Position

### TC-GS-POS-304: Mobile, screening toolbar dan tombol [+ Position]

13. Verifikasi Breadcrumb `User > Position`
14. Verifikasi sub-tab `User List | Position | Division | Custom Field`
15. Verifikasi toolbar `[⋯]`
16. Verifikasi toolbar `[🔍]`
17. Verifikasi `[+ Position]` tampil di bawah toolbar
18. Verifikasi `[+ Position]` tampil di atas card list
19. Tap `[⋯]` toolbar
20. Verifikasi bottom sheet berisi `Column Visibility`, `Filter`, `Download`, `Changelog`
21. Tutup bottom sheet
22. Tap `[🔍]`
23. Verifikasi Search bar inline muncul di halaman
24. Tutup Search bar inline

### TC-GS-POS-151: Mobile, long-press card masuk selection mode dan Bulk Delete

25. Long-press card `Account Executive {runId}-027`
26. Verifikasi checkbox muncul di tiap card
27. Verifikasi header berubah menjadi toolbar seleksi dengan teks `1 selected`
28. Verifikasi toolbar seleksi memuat `[Cancel]`
29. Verifikasi bottom bar memuat Delete
30. Tap card `Business Analyst {runId}-027`
31. Verifikasi card `Business Analyst {runId}-027` tercentang
32. Verifikasi tap card tidak membuka aksi lain
33. Tap Delete pada sticky bottom bar
34. Verifikasi Dialog Delete Position tampil sebagai bottom sheet
35. Verifikasi dialog memuat `• Account Executive {runId}-027`
36. Verifikasi dialog memuat `• Business Analyst {runId}-027`
37. Tap `[Delete]` pada dialog
38. Verifikasi toast sukses "Success, position has been deleted."
39. Verifikasi selection mode berakhir

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`. Spec mobile Android (`coverage.mobile: automated`), bentuk frontmatter mengikuti spec Brand E2E-074.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memuat 39 langkah (di atas smell sekitar 35 langkah). Alasan: seluruhnya satu kelas harness (mobile Android) pada satu perangkat; pemecahan menambah hook perangkat dan login. Ganti akun hanya satu kali (langkah 12), dan TC-GS-POS-151 yang menghapus data berada di akhir.
- Urutan TC dalam spec: 298 (akun Read-Only), ganti akun, 304, 151 (akun Total Control). Pengelompokan per akun menghasilkan satu kali ganti akun (langkah 12); TC-GS-POS-151 menghapus data dan ditaruh paling akhir. Urutan ini menyimpang dari urutan TC sumber (151, 298, 304).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7, 11, 21, dan 24 (menutup bottom sheet, opsi sort, dan Search bar sebelum langkah berikutnya).
- Langkah 12 (ganti akun) tidak tertulis di Langkah Uji TC sumber; Precondition TC-GS-POS-298 menyebut akun Read-Only dan TC-GS-POS-151 serta 304 menyebut akun Total Control. Layar awal User > Position (Precondition b TC-GS-POS-151, 298, dan 304) dibuka di hook `beforeEach`.
- Langkah 26 sampai 29 memecah Expected a TC-GS-POS-151 per klausa; langkah 32 berasal dari Expected b ("bukan membuka aksi lain").
- Langkah 5 dan 9 (Column Visibility dan opsi sort memuat `Name`) adalah klausa Expected b dan c TC-GS-POS-298 sekaligus pembanding positif bagi asersi absence `Last Updated` pada langkah 6 dan 10.
- Pembagian TC lintas spec: Bulk Delete web ada di spec 025 dan 026; Column Visibility web di spec 031.
- Temuan untuk QA:
  - TC-GS-POS-298 langkah 3 ("Buka opsi sort yang tersedia") tidak menyebut lokasi kontrol sort di mobile; spec membukanya tanpa menyebut elemen tertentu.
  - TC-GS-POS-298 Expected a menyebut `[⋯]` row action tidak tampil dengan alasan Edit dan Delete Hidden, sehingga Read-Only dan Manage user and role Read-Only diperlakukan sama; TC tidak memberi bukti terpisah untuk menu card lain.
  - TC-GS-POS-304 langkah 3 ("tap `[🔍]`") tidak menyebut cara menutup Search bar inline; spec menutupnya sebagai langkah penghubung tanpa menyebut elemen tertentu.
  - TC-GS-POS-151 langkah 3 menyebut "Tap Delete pada sticky bottom bar" tanpa teks tombol baku; label dialog `[Delete]` diikuti sesuai TC.
  - Kolom Automation TC-GS-POS-151, 298, dan 304 bernilai `Manual Only`; spec tetap ditulis sebagai `coverage.mobile: automated` mengikuti bagian 2 konvensi (kelayakan teknis bukan kriteria seleksi).
