---
id: TC-AC-ACC-E2E-066-edit-screening-popup-status-client-dan-field-reflected-af
title: "Popup Edit Client: Screening, Jalur Masuk, Field Reflected Derived, dan Aksi Client Suspended (Active-Full)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-135
  - TC-AC-ACC-136
  - TC-AC-ACC-946
  - TC-AC-ACC-138
  - TC-AC-ACC-161
  - TC-AC-ACC-1007
  - TC-AC-ACC-158
  - TC-AC-ACC-545
coverage:
  web: automated
---

# Popup Edit Client: Screening, Jalur Masuk, Field Reflected Derived, dan Aksi Client Suspended (Active-Full)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Active-Full (A-15) `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD`. Login akun Active-Full di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya. `{r6}` = 6 digit terakhir `{runId}` (dipakai agar Client Code tetap maksimal 15 karakter).
- Dataset seed (nama bersuffix, tidak memakai baris Pre-setup sebagai target): Client `PT Teknologi Maju {runId}-066` (replika C-02: Active, Partner CV Mitra Sejati sebagai Anchor dan CV Mitra Lestari, Group Area Jakarta, FAMS Grace, Photo tersimpan, Client Code `TKM-{r6}`, Default User Not Yet Activated dengan Division seed `Finance` dan Position seed `Finance Manager`); Client `PT Sejahtera Abadi {runId}-066` (replika C-01: Active, Partner CV Mitra Sejati, Group Area Jakarta, Client Code `SJA-{r6}`, Default User Activated, PIC Email awal `pic.old@example.com`); `PT Wahana Nusantara {runId}-066` (replika C-03: Suspended, FAMS Expired, SAMS Archive, pernah memiliki subscription); `PT Maju Bersama {runId}-066` (replika C-06: Active Derived, Group Area Jakarta, Client Code `MJB-{r6}`). Seeding Client lewat API/fixture BE di hook `before` (kemampuan disediakan tim FE/BE; endpoint tidak dikarang).
- Tabel Anggota Reflected (TC-161): Photo, Company Name, Company Email, Industry, Website, Fax, Address, Country, State, City, Postal Code, PIC Name, PIC Email, PIC Phone.
- Cleanup: hook `after` menghapus lewat API (soft-delete) Client yang dibuat atau di-seed spec ini, tanpa mengasumsikan setup berhasil penuh. Client Code `MJB9-{r6}` hasil TC-1007 dipulihkan oleh cleanup (Client seed dihapus).
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

### TC-135: Screening popup Edit Default User Not Yet Activated

1. Ketik Search `PT Teknologi Maju {runId}-066`, tekan Enter
2. Buka `⋯` baris `PT Teknologi Maju {runId}-066` lalu klik `Edit`
3. Verifikasi header popup: Title "Edit Client" dan tombol `[✕]`
4. Verifikasi body: field sama dengan Create terisi nilai saat ini (termasuk Photo)
5. Verifikasi Client Code wajib
6. Verifikasi Partner read-only
7. Verifikasi Select Group tersembunyi (Client punya relasi manager)
8. Verifikasi Section Default User tampil dan dapat diedit: First Name, Last Name, Email
9. Verifikasi Division (dropdown single-select) terisi "Finance"
10. Verifikasi Position (dropdown single-select opsional) terisi "Finance Manager"
11. Kosongkan pilihan Division
12. Verifikasi Division menampilkan placeholder "Select division"
13. Kosongkan pilihan Position
14. Verifikasi Position menampilkan placeholder "Select position"
15. Verifikasi footer memuat `[Clear Field]` dan `[Save]` (Success)
16. Klik `[✕]` di header popup
17. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]` tampil
18. Klik `[Leave]`

### TC-136 dan TC-946: Default User Activated dan footer tanpa Stay

19. Ketik Search `PT Sejahtera Abadi {runId}-066`, tekan Enter
20. Buka `⋯` baris `PT Sejahtera Abadi {runId}-066` lalu klik `Edit`
21. Verifikasi Section Default User tidak tampil
22. Verifikasi field identitas Client lain terisi dan dapat diedit
23. Verifikasi footer popup "Edit Client" memuat `[Clear Field]` dan `[Save]`
24. Verifikasi footer tidak memuat checkbox maupun teks "Stay on this form after submitting"
25. Klik `[✕]` di header popup

### TC-138: Jalur masuk kedua lewat Detail

26. Klik Company Name `PT Sejahtera Abadi {runId}-066` untuk membuka Detail
27. Klik `[Edit]` di header Detail
28. Verifikasi popup Edit Client terbuka dengan Title "Edit Client"
29. Verifikasi Company Name terisi "PT Sejahtera Abadi {runId}-066" dan Client Code terisi "SJA-{r6}"
30. Verifikasi footer memuat `[Clear Field]` dan `[Save]`
31. Klik `[✕]` di header popup
32. Klik breadcrumb "Client" untuk kembali ke List

### TC-161 dan TC-1007: Client Derived

33. Ketik Search `PT Maju Bersama {runId}-066`, tekan Enter
34. Buka `⋯` baris `PT Maju Bersama {runId}-066` lalu klik `Edit`
35. Untuk setiap anggota pada tabel Anggota Reflected, lakukan langkah 36 sampai 37
36. Coba ubah (untuk Photo: ganti atau hapus) anggota
37. Verifikasi anggota read-only (tidak dapat diubah)
38. Verifikasi field Client Code tidak read-only dan dapat diubah (milik Client, bukan field Reflected)
39. Verifikasi field Select Group tidak tampil di form Edit (Group Client Derived mengikuti Anchor entitas induk)
40. Ubah Client Code menjadi `MJB9-{r6}`
41. Klik `[Save]`
42. Verifikasi popup tertutup
43. Verifikasi toast sukses "Success, client has been updated."
44. Klik Company Name `PT Maju Bersama {runId}-066` untuk membuka Detail
45. Verifikasi Detail menampilkan Client Code "MJB9-{r6}"
46. Verifikasi Company Name "PT Maju Bersama {runId}-066" tidak berubah
47. Verifikasi badge `Derived` tetap
48. Klik breadcrumb "Client" untuk kembali ke List

### TC-158 dan TC-545: Aksi Client Suspended

49. Klik sub-tab Suspended
50. Ketik Search `PT Wahana Nusantara {runId}-066`, tekan Enter
51. Buka `⋯` baris "PT Wahana Nusantara {runId}-066"
52. Verifikasi menu `⋯` memuat `Detail` dan `Unsuspend`
53. Verifikasi `Edit`, `Change Partner`, `Suspend`, dan `Delete` Hidden (Delete Hidden karena Client pernah memiliki subscription)
54. Klik Company Name `PT Wahana Nusantara {runId}-066` untuk membuka Detail
55. Verifikasi header menampilkan Company Name "PT Wahana Nusantara {runId}-066" dan badge `Suspended`
56. Verifikasi tombol `[Edit]` di pojok kanan atas header Hidden

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Alasan di atas 35 langkah (sekitar 70 langkah): seluruh blok adalah observasi popup Edit dan status Client oleh satu role; satu-satunya aksi tulis adalah Client Code Derived (TC-1007) di akhir blok Derived. Setiap blok memakai Client seed milik sendiri dan berdiri sendiri. Langkah 36 sampai 37 diulang untuk 14 anggota.
- Langkah penghubung (S-03): Search nama unik; `✕` menutup popup pristine; sub-tab dan breadcrumb. Kondisi "mengosongkan Division dan Position" TC-135 membuat form dirty sehingga ditutup lewat dialog `Unsaved Changes` dan `[Leave]` (S-08).
- Temuan untuk QA:
  - TC-161 langkah 4 ("Coba ubah atau hapus ... satu per satu") tidak menyebut cara mengamati read-only (disabled atau readonly); spec memakai redaksi TC.
  - TC-1007 mengubah Client Code Derived ke `MJB-906`; spec memakai `MJB9-{r6}` agar unik per run.
