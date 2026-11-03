---
id: TC-AC-SU-E2E-085-user-list-column-visibility-dan-setup-column-default-visible
title: "User List Column Visibility dan Setup Column: Kolom Default Visible"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-303
  - TC-AC-SU-304
  - TC-AC-SU-305
  - TC-AC-SU-306
  - TC-AC-SU-307
coverage:
  web: automated
---

# User List Column Visibility dan Setup Column: Kolom Default Visible

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` dan kemampuan Fixture BE mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (di-seed hook `before` lewat Fixture BE; nama bersuffix `{runId}-085`): `John Doe {runId}-085` dan `Jane Smith {runId}-085` (Active, Activated, seluruh kolom default visible terisi; dipakai sebagai precondition TC, tidak diasersi). Live Preview menampilkan data entitas Principal dengan format yang sama dengan tabel.
- Viewport: lebar 1280px diatur oleh langkah 38 (awal TC-307) agar tabel dapat di-scroll horizontal, dan dipulihkan ke ukuran semula oleh langkah 52 serta hook `after`.
- Kolom default visible (parameter TC-305 sampai TC-307): Active, Name, Email, Role, Position, Division, Employee ID, Modified By, Last Updated.
- Hook `after` menghapus data yang di-seed hook `before` spec ini lewat Fixture BE; pembersihan tidak berasumsi seeding berhasil penuh.
- Pemulihan Setup Column: preferensi kolom yang disimpan spec ini dihapus di hook `after` dengan menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan ini disediakan tim FE.

## Test Steps

### TC-AC-SU-303: Screening Overlay Column Visibility User List

1. Hover icon `⋯` pada header Actions
2. Verifikasi tooltip `Column Visibility` tampil
3. Klik icon `⋯`
4. Verifikasi overlay memuat CTA `[Setup Column]` di atas
5. Verifikasi daftar kolom urut default: Active ☑ | Name ☑ | Email ☑ | Role ☑ | Position ☑ | Division ☑ | Employee ID ☑ | Modified By ☑ | Last Updated ☑ | Activation Status ☐ | Temporary User ☐ | Temporary Until ☐ | TAG ☐ | [Custom Field aktif] ☐
6. Verifikasi semua kolom pada daftar enabled
7. Verifikasi drag handle tersedia pada tiap kolom
8. Tekan Esc untuk menutup overlay

### TC-AC-SU-304: Screening Popup Setup Column dan Live Preview

9. Klik `⋯` pada header Actions
10. Klik `[Setup Column]`
11. Verifikasi header popup: Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan icon (X)
12. Verifikasi body popup: daftar kolom dengan checkbox, drag handle, dan icon Pin
13. Verifikasi Live Preview menampilkan header dan data entitas dengan format yang sama dengan tabel
14. Verifikasi footer `[Reset to Default]` dan `[Save]` rata kanan
15. Verifikasi footer tanpa `[Cancel]`
16. Klik icon (X) pada popup

### TC-AC-SU-305: Setup Column ceklis dan unceklis kelas default visible

17. Klik `⋯` pada header Actions
18. Klik `[Setup Column]`
19. Hapus centang kolom Active, Email, Role, Position, Division, Employee ID, Modified By, dan Last Updated satu per satu (kolom Name disisakan)
20. Verifikasi Live Preview memuat kolom `Name`
21. Verifikasi Live Preview tidak memuat kolom Active, Email, Role, Position, Division, Employee ID, Modified By, dan Last Updated
22. Klik `[Save]`
23. Verifikasi tabel memuat kolom `Name`
24. Verifikasi tabel tidak memuat kolom Active, Email, Role, Position, Division, Employee ID, Modified By, dan Last Updated
25. Tekan F5
26. Verifikasi tabel memuat kolom `Name`
27. Verifikasi konfigurasi bertahan: tabel tetap tidak memuat kolom Active, Email, Role, Position, Division, Employee ID, Modified By, dan Last Updated
28. Klik `⋯` pada header Actions, klik `[Setup Column]`, klik `[Reset to Default]`, klik `[Save]`

### TC-AC-SU-306: Setup Column drag reorder kelas default visible

29. Klik `⋯` pada header Actions
30. Klik `[Setup Column]`
31. Drag tiap kolom default visible ke posisi lain sehingga urutannya menjadi: Last Updated, Modified By, Employee ID, Division, Position, Role, Email, Name, Active
32. Verifikasi urutan baru tampil di Live Preview
33. Klik `[Save]`
34. Verifikasi urutan baru tampil di tabel
35. Tekan F5
36. Verifikasi urutan baru bertahan di tabel
37. Klik `⋯` pada header Actions, klik `[Setup Column]`, klik `[Reset to Default]`, klik `[Save]`

### TC-AC-SU-307: Setup Column pin dan unpin kelas default visible

38. Atur lebar viewport menjadi 1280px sehingga tabel dapat di-scroll horizontal
39. Klik `⋯` pada header Actions
40. Klik `[Setup Column]`
41. Klik icon Pin pada kolom Active, Name, Email, Role, Position, Division, Employee ID, Modified By, dan Last Updated satu per satu
42. Klik `[Save]`
43. Scroll tabel secara horizontal
44. Verifikasi kolom ter-pin tetap terlihat saat tabel di-scroll
45. Tekan F5
46. Scroll tabel secara horizontal
47. Verifikasi pin bertahan setelah F5
48. Klik `⋯` pada header Actions, klik `[Setup Column]`
49. Klik icon Pin (unpin) pada kolom yang ter-pin satu per satu, klik `[Save]`
50. Scroll tabel secara horizontal
51. Verifikasi kolom ikut ter-scroll setelah unpin
52. Pulihkan lebar viewport ke ukuran semula

## Notes

- Langkah penghubung (S-03): langkah 38 mengatur lebar viewport dan langkah 52 memulihkannya; Esc menutup overlay Column Visibility; langkah `[Reset to Default]` lalu `[Save]` di akhir TC-305 dan TC-306 mengembalikan konfigurasi supaya TC berikutnya tidak mewarisi urutan atau visibilitas (S-09). Semua langkah ubah-simpan kolom dipulihkan juga oleh hook `after`.
- Langkah 20, 23, dan 26 (`Verifikasi` kolom `Name` tampil) adalah asersi tambahan (S-03, dasar 8b.2): kolom `Name` yang disisakan menjadi anchor positif bagi absence kolom lain pada langkah 21, 24, dan 27.
- Pada TC-305 sampai TC-307 pengulangan per kolom ditulis sebagai satu langkah daftar kolom (aksi identik per kolom); `Verifikasi` Live Preview dan tabel menyebut seluruh kolom sebagai daftar elemen yang sama.
- Alasan di atas ±35 langkah: kelima TC adalah Column Visibility dan Setup Column User List dengan dataset yang sama dan berdiri sendiri; kegagalan satu TC tidak membuat TC lain kehilangan makna.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-085` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-305 sampai TC-307 meminta mengamati Live Preview "satu per satu"; spec menghapus centang semua kolom lebih dulu lalu mengasersi Live Preview sekali (final state).
  - TC-306 dan TC-307 menyebut "Drag tiap kolom Data Uji ke posisi lain" tanpa urutan tujuan; spec memakai urutan terbalik dari default.
