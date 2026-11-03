---
id: TC-AC-ACC-E2E-139-bulk-suspend-client-derived-campuran-dan-blok
title: "Bulk Suspend dengan Client Derived: Dialog Campuran dengan [Continue] dan Dialog Blok D-15 Tanpa Toast Sukses"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-212
  - TC-AC-ACC-213
coverage:
  web: automated
---

# Bulk Suspend dengan Client Derived: Dialog Campuran dengan [Continue] dan Dialog Blok D-15 Tanpa Toast Sukses

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Active-Full A-15 `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password dari `AC_CLIENT_ACTIVE_FULL_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Data Pre-setup: C-06 `PT Maju Bersama` (Active, Derived) hanya dibaca (di-skip oleh Bulk Suspend).
- Fixture milik spec (Fixture BE, disediakan tim FE/BE; seed di hook `before`, cleanup di hook `after`; S-06, S-12): `PT Sejahtera Abadi {runId}-139` (setara C-01: Active, Partner CV Mitra Sejati, Group Area Jakarta, FAMS, SAMS, SIEM Active) adalah target Suspend; efek: baris Changelog `Suspend` dan Last Updated replika bertambah, hanya pada data milik spec ini. Client C-01 `PT Sejahtera Abadi` literal tidak disentuh.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-213: Bulk Suspend seluruh baris terpilih adalah Client Derived: dialog blok D-15 langsung tampil

1. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Maju Bersama` lalu tekan Enter
2. Ubah ukuran halaman modal menjadi 100, catat jumlah baris Action `Suspend` untuk "PT Maju Bersama" (N1), lalu tutup modal
3. Klik sub-tab Active, ketik Search `PT Maju Bersama`, tekan Enter
4. Centang baris `PT Maju Bersama` (Derived)
5. Klik Bulk Action lalu pilih `Suspend`
6. Verifikasi dialog blok Title "Unable to Suspend Clients" langsung tampil
7. Verifikasi dialog blok memuat bullet `• PT Maju Bersama`
8. Verifikasi dialog blok memuat "The selected clients cannot be suspended because they are already suspended, archived, or are derived clients."
9. Verifikasi dialog blok memuat tombol `[OK]` dengan lebar 480px
10. Verifikasi dialog konfirmasi Title "Suspend Clients" tidak tampil
11. Klik `[OK]`
12. Verifikasi tidak ada toast sukses
13. Verifikasi tidak ada toast ringkasan "Some items were skipped."
14. Verifikasi baris `PT Maju Bersama` tetap tampil di sub-tab Active
15. Verifikasi checkbox baris `PT Maju Bersama` tetap tercentang
16. Verifikasi Bulk Action Bar tetap tampil (seleksi dipertahankan setelah dialog blok D-15)
17. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Maju Bersama` lalu tekan Enter, ubah ukuran halaman modal menjadi 100
18. Verifikasi jumlah baris Action `Suspend` untuk "PT Maju Bersama" tetap N1 (tidak ada baris baru)
19. Tutup modal Changelog, lalu klik ikon (X) pada Bulk Action Bar

### TC-AC-ACC-212: Bulk Suspend baris Active + Client Derived: dialog campuran dua kelompok bullet dengan [Continue]

20. Klik `[Changelog]` di toolbar List, ketik `PT Sejahtera Abadi {runId}-139` di Search modal lalu tekan Enter, ubah ukuran halaman modal menjadi 100, lalu catat jumlah baris Action `Suspend` (N1)
21. Ganti isi Search modal dengan `PT Maju Bersama` lalu tekan Enter, catat jumlah baris Action `Suspend` (N2), lalu tutup modal
22. Klik sub-tab Active lalu ketik Search `PT Sejahtera Abadi {runId}-139` dan tekan Enter
23. Centang baris `PT Sejahtera Abadi {runId}-139`
24. Ganti isi Search dengan `PT Maju Bersama`, tekan Enter
25. Centang baris `PT Maju Bersama` (Derived)
26. Klik Bulk Action lalu pilih `Suspend`
27. Verifikasi dialog Title "Suspend Clients"
28. Verifikasi kelompok "The following will be suspended:" berisi bullet `• PT Sejahtera Abadi {runId}-139`
29. Verifikasi kelompok "The following will be skipped:" berisi bullet `• PT Maju Bersama`
30. Verifikasi kalimat "Are you sure you want to continue?"
31. Verifikasi footer memuat `[Cancel]` dan `[Continue]`
32. Klik `[Continue]`
33. Verifikasi toast "Success, client has been suspended. Some items were skipped."
34. Verifikasi tidak ada dialog blok
35. Verifikasi Bulk Action Bar hilang
36. Verifikasi tidak ada baris tercentang
37. Klik sub-tab Active, ketik Search `PT Maju Bersama`, tekan Enter
38. Verifikasi baris `PT Maju Bersama` tetap tampil di sub-tab Active
39. Klik sub-tab Suspended, ketik Search `PT Sejahtera Abadi {runId}-139`, tekan Enter
40. Verifikasi baris `PT Sejahtera Abadi {runId}-139` tampil di sub-tab Suspended
41. Klik `[Changelog]` di toolbar List, ketik `PT Sejahtera Abadi {runId}-139` di Search modal lalu tekan Enter, ubah ukuran halaman modal menjadi 100, lalu catat jumlah baris Action `Suspend` (N3)
42. Ganti isi Search modal dengan `PT Maju Bersama` lalu tekan Enter dan catat jumlah baris Action `Suspend` (N4)
43. Verifikasi N3 adalah N1 + 1
44. Verifikasi N4 adalah N2 (tidak ada baris `Suspend` baru untuk "PT Maju Bersama")
45. Tutup modal Changelog

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini melewati sekitar 35 langkah: satu `Verifikasi` per klausa Expected (S-01) dan baseline Changelog (S-12) atas dua TC satu topik (Bulk Suspend dengan Client Derived), satu akun; blok dialog blok D-15 (tanpa mengubah data) mendahului blok yang mengubah status (TC-AC-ACC-212, di akhir) sehingga tetap bermakna walau blok sebelumnya gagal.
- Urutan TC-AC-ACC-213 sebelum TC-AC-ACC-212 menyimpang dari urutan nomor karena TC-AC-ACC-212 mengubah status `PT Sejahtera Abadi` dan menaruh aksi pengubah data di akhir (prinsip 5); alasan dicatat di sini (S-05).
- Langkah penghubung (tanpa awalan Verifikasi): klik (X) menutup Bulk Action Bar (langkah 19), penutupan modal Changelog, dan Search yang menemukan baris target (R-16).
- Post Condition TC-AC-ACC-212 (Unsuspend `PT Sejahtera Abadi`) tidak dijalankan karena target adalah replika milik spec yang dibersihkan hook `after`.
- Post Condition TC-AC-ACC-213: `-`. Asersi absence toast (langkah 12 dan 13) berlandaskan dialog blok yang sudah diasersi dan ditutup sebagai anchor positif (butir 11 bagian 8b).
- Temuan untuk QA:
  - TC-AC-ACC-213 Expected c ("seleksi dipertahankan") menyebut checkbox tercentang dan Bulk Action Bar tetap tampil, sedangkan TC-AC-ACC-212 Expected b menyebut seleksi di-reset ke 0 setelah toast ringkasan; kedua perilaku konsisten dengan `prd-conventions.md` ("Perilaku Setelah Bulk Action Selesai") dan diasersi sesuai TC masing-masing.
