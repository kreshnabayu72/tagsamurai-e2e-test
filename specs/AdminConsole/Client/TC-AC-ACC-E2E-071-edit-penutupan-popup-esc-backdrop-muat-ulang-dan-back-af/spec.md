---
id: TC-AC-ACC-E2E-071-edit-penutupan-popup-esc-backdrop-muat-ulang-dan-back-af
title: "Popup Edit Client: Penutupan dengan ✕, Esc, Backdrop, F5, dan Tombol Back (Active-Full)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-470
  - TC-AC-ACC-550
  - TC-AC-ACC-520
  - TC-AC-ACC-166
  - TC-AC-ACC-469
  - TC-AC-ACC-548
  - TC-AC-ACC-549
  - TC-AC-ACC-551
  - TC-AC-ACC-552
coverage:
  web: automated
---

# Popup Edit Client: Penutupan dengan ✕, Esc, Backdrop, F5, dan Tombol Back (Active-Full)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Active-Full (A-15) `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD`. Login akun Active-Full di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya. `{r6}` = 6 digit terakhir `{runId}` (dipakai agar Client Code tetap maksimal 15 karakter).
- Dataset seed (nama bersuffix): Client `PT Sejahtera Abadi {runId}-071` (replika C-01: Active, Partner CV Mitra Sejati, Group Area Jakarta, Client Code `SJA-{r6}`, Default User Activated, PIC Email awal `pic.old@example.com`) dengan Fax kosong. Seeding Client lewat API/fixture BE di hook `before` (kemampuan disediakan tim FE/BE; endpoint tidak dikarang).
- Nilai uji Fax: `0215550123`, `0215550124`. Kemampuan teknis: mengonfirmasi atau menolak dialog `beforeunload` bawaan browser pada F5, menekan Esc, tombol Back browser, dan klik area di luar popup (butir S-08: kemampuan `beforeunload` tertulis di sini).
- Perubahan yang disimpan TC-551 (Fax `0215550124`) memengaruhi hanya Client seed spec ini; cleanup menghapus Client seed.
- Cleanup: hook `after` menghapus lewat API (soft-delete) Client yang dibuat atau di-seed spec ini, tanpa mengasumsikan setup berhasil penuh.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

### TC-470: Tutup popup tanpa perubahan

1. Ketik Search `PT Sejahtera Abadi {runId}-071`, tekan Enter
2. Buka `⋯` baris `PT Sejahtera Abadi {runId}-071` lalu klik `Edit`
3. Klik `[✕]` di header popup
4. Verifikasi popup tertutup langsung tanpa dialog
5. Buka `⋯` baris `PT Sejahtera Abadi {runId}-071` lalu klik `Edit`
6. Tekan Esc
7. Verifikasi popup tertutup langsung tanpa dialog

### TC-550: F5 tanpa perubahan

8. Buka `⋯` baris `PT Sejahtera Abadi {runId}-071` lalu klik `Edit`
9. Tekan F5 tanpa mengubah field apa pun
10. Verifikasi halaman dimuat ulang tanpa konfirmasi bawaan browser

### TC-520, TC-166, TC-469: Klik backdrop, ✕, Cancel, Leave

11. Ketik Search `PT Sejahtera Abadi {runId}-071`, tekan Enter
12. Buka `⋯` baris `PT Sejahtera Abadi {runId}-071` lalu klik `Edit`
13. Ubah Fax menjadi `0215550123`
14. Klik area di luar popup (backdrop)
15. Verifikasi popup Edit Client tetap terbuka
16. Verifikasi Fax masih "0215550123"
17. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" tidak muncul
18. Klik `[✕]` di header popup
19. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]` tampil
20. Klik `[Cancel]`
21. Verifikasi dialog tertutup
22. Verifikasi popup Edit tetap terbuka
23. Verifikasi Fax tetap "0215550123"
24. Klik `[✕]` di header popup lagi
25. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]` tampil
26. Klik `[Leave]`
27. Verifikasi popup tertutup tanpa menyimpan
28. Buka `⋯` baris `PT Sejahtera Abadi {runId}-071` lalu klik `Edit`
29. Verifikasi Fax tersimpan semula (kosong)

### TC-548: Ubah lalu kembalikan ke nilai identik

30. Ketik "9" di akhir field Fax
31. Tekan Backspace satu kali
32. Klik `[✕]` di header popup
33. Verifikasi popup tertutup langsung
34. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" tidak muncul

### TC-549: F5 saat popup berubah

35. Buka `⋯` baris `PT Sejahtera Abadi {runId}-071` lalu klik `Edit`
36. Ubah Fax menjadi `0215550123`
37. Tekan F5
38. Verifikasi konfirmasi bawaan browser muncul (teks dan tombol ditentukan browser)
39. Pilih tetap berada di halaman pada konfirmasi bawaan browser
40. Verifikasi popup Edit tetap terbuka
41. Verifikasi Fax masih "0215550123"
42. Klik `[✕]` di header popup
43. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]` tampil
44. Klik `[Leave]`

### TC-551: F5 sesudah Save berhasil

45. Buka `⋯` baris `PT Sejahtera Abadi {runId}-071` lalu klik `Edit`
46. Ubah Fax menjadi `0215550124`
47. Klik `[Save]`
48. Verifikasi popup tertutup
49. Verifikasi toast sukses "Success, client has been updated."
50. Tekan F5
51. Verifikasi halaman dimuat ulang tanpa konfirmasi bawaan browser

### TC-552: Tombol Back browser saat popup berubah

52. Ketik Search `PT Sejahtera Abadi {runId}-071`, tekan Enter
53. Buka `⋯` baris `PT Sejahtera Abadi {runId}-071` lalu klik `Edit`
54. Ubah Fax menjadi `0215550123`
55. Tekan tombol Back browser
56. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]` tampil
57. Klik `[Cancel]`
58. Verifikasi dialog tertutup
59. Verifikasi halaman tetap di Client
60. Verifikasi popup Edit tetap terbuka
61. Verifikasi Fax masih "0215550123"
62. Tekan tombol Back browser lagi
63. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]` tampil
64. Klik `[Leave]`
65. Verifikasi navigasi Back berjalan
66. Verifikasi popup Edit tertutup tanpa menyimpan

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Alasan di atas 35 langkah (sekitar 75 langkah): satu role, satu Client seed, satu kelas (penutupan popup Edit); jumlah buka form sama dengan jumlah kejadian menutup (prinsip 6); TC-552 di akhir karena Back meninggalkan halaman; TC-551 menyimpan Fax pada Client seed sehingga ditaruh sesudah kasus yang memerlukan Fax kosong.
- Langkah penghubung (S-03): Search ulang sesudah F5 memuat ulang List; "Ketik 9 di akhir field Fax" memakai popup Edit hasil buka ulang TC-469 (form baru).
- Temuan untuk QA:
  - TC-469 butir c ("Edit berikutnya menampilkan Fax tersimpan semula") dan TC-166 (tanpa Expected terpisah untuk pemulihan) tumpang tindih dengan TC-520; spec menjalankan satu urutan dan mengasersi tiap Expected sekali.
