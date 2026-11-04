---
id: TC-AC-SU-E2E-091-perubahan-custom-field-global-settings-terhadap-user-list-bagian-1
title: "Perubahan Custom Field di Global Settings terhadap User List dan Detail User (bagian 1)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SU-328
  - TC-AC-SU-330
  - TC-AC-SU-667
  - TC-AC-SU-608
  - TC-AC-SU-329
coverage:
  web: automated
---

# Perubahan Custom Field di Global Settings terhadap User List dan Detail User (bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` dan kemampuan Fixture BE mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Custom Field User milik spec (di-seed hook `before` lewat Fixture BE; nama bersuffix `{runId}-091`, entitas Principal, Global Settings > User > Custom Field): `Office Location {runId}-091` (Text, Active), `Shift {runId}-091` (Dropdown: `Day`, `Night`, Active), `Emergency Phone {runId}-091` (Phone, Active), `Blood Type {runId}-091` (Dropdown, Active). State Custom Field User adalah state global; hook `after` menghapus keempat field dan memulihkan Custom Field User ke keadaan awal (suite serial).
- Data Dinamis (nama bersuffix `{runId}-091`): `John Doe {runId}-091` (`Emergency Phone {runId}-091` = Country Code `🇮🇩 +62` dan Number `81234567890`, `Shift {runId}-091` = `Day`), `Jane Smith {runId}-091` (`Shift {runId}-091` = `Night`), `Mike Tan {runId}-091` (`Blood Type {runId}-091` = `O`), `Sarah Lee {runId}-091` (tanpa nilai `Emergency Phone {runId}-091`).
- Langkah di Global Settings > User > Custom Field dijalankan lewat UI Global Settings oleh aktor yang sama (akses Total Control).
- Hook `after` menghapus data yang di-seed hook `before` spec ini lewat Fixture BE; pembersihan tidak berasumsi seeding berhasil penuh.
- Pemulihan Setup Column: preferensi kolom yang disimpan spec ini dihapus di hook `after` dengan menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan ini disediakan tim FE.

## Test Steps

### TC-AC-SU-328: Custom Field yang sedang tampil sebagai kolom di-deactivate

1. Klik `⋯` pada header Actions
2. Klik `[Setup Column]`
3. Centang kolom `Office Location {runId}-091`, klik icon Pin pada `Office Location {runId}-091`
4. Klik `[Save]`
5. Buka Global Settings > User > Custom Field
6. Nonaktifkan (Deactivate) `Office Location {runId}-091`, klik konfirmasi
7. Tunggu aksi selesai
8. Buka Settings > User
9. Verifikasi kolom `Name` tampil di tabel User List
10. Verifikasi kolom Custom Field aktif `Office Location {runId}-091` tidak lagi tampil di tabel User List
11. Klik `⋯` pada header Actions, klik `[Setup Column]`
12. Verifikasi `Shift {runId}-091` ada di daftar kolom Popup Setup Column
13. Verifikasi `Office Location {runId}-091` tidak ada di daftar kolom Popup Setup Column
14. Klik icon (X) pada popup

### TC-AC-SU-330: Custom Field di-activate kembali tampil sebagai kolom curated default Hidden

15. Buka Global Settings > User > Custom Field
16. Aktifkan (Activate) `Office Location {runId}-091`, klik konfirmasi
17. Tunggu aksi selesai
18. Buka Settings > User
19. Verifikasi kolom `Name` tampil di tabel User List
20. Verifikasi kolom `Office Location {runId}-091` tidak tampil di tabel (default Hidden)
21. Klik `⋯` pada header Actions, klik `[Setup Column]`
22. Verifikasi `Office Location {runId}-091` tercantum sebagai curated unchecked
23. Verifikasi `Office Location {runId}-091` tanpa pin
24. Klik icon (X) pada popup

### TC-AC-SU-667: Kolom curated Custom Field Phone menampilkan nilai `[+CountryCode] [Number]`

25. Klik `⋯` pada header Actions
26. Klik `[Setup Column]`
27. Centang `Emergency Phone {runId}-091`, klik `[Save]`
28. Verifikasi kolom `Emergency Phone {runId}-091` tampil
29. Ketik Search `{runId}-091`, tekan Enter
30. Verifikasi sel `Emergency Phone {runId}-091` baris `John Doe {runId}-091` berisi `+62 81234567890` (satu spasi)
31. Verifikasi nilai tidak tampil tanpa spasi (`+6281234567890`)
32. Verifikasi sel `Emergency Phone {runId}-091` baris user tanpa nilai (`Sarah Lee {runId}-091`) berisi `—`

### TC-AC-SU-608: Custom Field baru aktif di Global Settings muncul sebagai kolom curated dan di accordion

33. Klik `⋯` pada header Actions
34. Klik `[Setup Column]`
35. Verifikasi `Blood Type {runId}-091` ada di daftar Setup Column dan default unchecked
36. Centang `Blood Type {runId}-091`, klik `[Save]`
37. Verifikasi kolom `Blood Type {runId}-091` tampil dengan nilai `O` pada baris `Mike Tan {runId}-091`
38. Ganti isi kotak Search dengan `Mike Tan {runId}-091`, tekan Enter
39. Buka Detail `Mike Tan {runId}-091`, expand accordion Custom Field
40. Verifikasi accordion menampilkan `Blood Type {runId}-091: O`
41. Klik breadcrumb `User` untuk kembali ke Settings > User
42. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-AC-SU-329: Filter Custom Field yang sedang aktif saat field dihapus

43. Klik icon Filter
44. Pilih field `Shift {runId}-091` = `Night`, klik `[Apply]`
45. Verifikasi baris `Jane Smith {runId}-091` (`Night`) tampil
46. Verifikasi baris `John Doe {runId}-091` (`Day`) tidak tampil
47. Buka Global Settings > User > Custom Field
48. Hapus (Delete) `Shift {runId}-091`, klik konfirmasi
49. Tunggu aksi selesai
50. Buka Settings > User
51. Ketik Search `{runId}-091`, tekan Enter
52. Klik icon Filter
53. Verifikasi field filter `Status` ada di Filter Panel
54. Verifikasi field filter `Shift {runId}-091` tidak ada di Filter Panel
55. Verifikasi kolom `Name` tampil di tabel User List
56. Klik `⋯` pada header Actions, klik `[Setup Column]`
57. Verifikasi `Blood Type {runId}-091` ada di daftar kolom Popup Setup Column
58. Verifikasi kolom `Shift {runId}-091` tidak ada di tabel
59. Verifikasi kolom `Shift {runId}-091` tidak ada di Popup Setup Column

## Notes

- Urutan spec: TC-330 langsung sesudah TC-328 karena TC-330 bergantung pada hasil TC-328 (Dependensi TC); TC-329 (menghapus field) di akhir (S-10).
- Langkah penghubung (S-03): mem-pin dan menampilkan `Office Location {runId}-091` pada TC-328 memenuhi precondition ("kolomnya sudah ditampilkan" dan "di-pin"); icon (X) menutup popup tanpa menyimpan; klik breadcrumb `User` kembali ke List; `(←)` pada kotak Search menutup input dan mereset tabel sebelum Filter karena Search `Mike Tan {runId}-091` dari TC-608 masih aktif sesudah kembali dari Detail (S-09, R-16).
- Langkah penghubung (S-03, R-16): "Ketik Search `{runId}-091`, tekan Enter" (langkah 29 dan 51) membatasi User List ke empat user seed milik spec (keyword hanya cocok dengan nama bersuffix seed) sebelum verifikasi sel dan baris; Search langkah 29 tetap aktif sampai langkah 37, sehingga langkah 38 memakai "Ganti isi kotak Search dengan `Mike Tan {runId}-091`, tekan Enter" untuk menemukan baris target sebelum Buka Detail; langkah 51 memakai "Ketik Search" karena kotak bersih sesudah navigasi sidebar; "Tunggu aksi selesai" setelah tiap aksi konfirmasi Global Settings (Deactivate, Activate, Delete) memberi waktu aksi selesai sebelum pindah ke Settings > User (bagian 8b butir 8); tanpa `Verifikasi`.
- Tiap asersi absence (kolom, opsi Setup Column, field filter) didahului `Verifikasi` pembanding pada surface yang sama: kolom `Name`, `Shift {runId}-091`, `Status`, dan `Blood Type {runId}-091` yang masih ada (bagian 8b butir 2).
- Alasan di atas ±35 langkah: kelima TC adalah dampak Custom Field User terhadap User List, dataset sama; TC-609 sampai TC-613 ada di spec 092.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-091` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-328 dan TC-329 memakai Custom Field `Office Location` dan `Shift` Pre-setup; spec memakai field milik spec bernama bersuffix karena menonaktifkan atau menghapus field Pre-setup melanggar S-06.
  - TC-329 mengharapkan kriteria filter `Shift` dilepas dan tabel dimuat ulang tanpa kriteria itu, tetapi spec kembali ke Settings > User lewat sidebar dan sidebar mereset Search, Sort, dan Filter; retensi Filter lintas navigasi sidebar belum dikonfirmasi FE dan TC-329 ambigu, sehingga kedua asersi tersebut tidak ditulis. Asersi absence field/kolom `Shift {runId}-091` tetap berlaku.
  - TC-330 precondition b menyebut `Office Location` "di-pin" tetapi TC-328 hanya menampilkan; spec mem-pin pada TC-328.
