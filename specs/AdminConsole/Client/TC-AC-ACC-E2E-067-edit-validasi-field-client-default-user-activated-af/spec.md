---
id: TC-AC-ACC-E2E-067-edit-validasi-field-client-default-user-activated-af
title: "Validasi Edit: Field Identitas Client Diblokir dan Duplikat Ditolak (Active-Full)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-142
  - TC-AC-ACC-143
  - TC-AC-ACC-144
  - TC-AC-ACC-145
  - TC-AC-ACC-146
  - TC-AC-ACC-147
  - TC-AC-ACC-148
  - TC-AC-ACC-149
  - TC-AC-ACC-523
  - TC-AC-ACC-524
  - TC-AC-ACC-525
  - TC-AC-ACC-526
  - TC-AC-ACC-529
  - TC-AC-ACC-536
  - TC-AC-ACC-537
  - TC-AC-ACC-944
coverage:
  web: automated
---

# Validasi Edit: Field Identitas Client Diblokir dan Duplikat Ditolak (Active-Full)

## Prerequisites

- Mode: FE+BE. Semua `[Save]` diblokir; tidak ada data Client yang berubah.
- Akun aktor: Active-Full (A-15) `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD`. Login akun Active-Full di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya. `{r6}` = 6 digit terakhir `{runId}` (dipakai agar Client Code tetap maksimal 15 karakter).
- Dataset seed (target Edit): Client `PT Sejahtera Abadi {runId}-067` (replika C-01: Active, Partner CV Mitra Sejati, Group Area Jakarta, Client Code `SJA-{r6}`, Default User Activated, PIC Email awal `pic.old@example.com`); Client `PT Menteng Jeda {runId}-067` (replika C-ROL-17: Direct, Group Cabang Menteng, Client Code `MJD-{r6}`). Sumber duplikat (data Pre-setup yang hanya dibaca dan hanya diketik sebagai nilai uji, tidak diubah): Company Name C-02 `PT Teknologi Maju`, Client Code C-02 `TKM-002`. Seeding Client lewat API/fixture BE di hook `before` (kemampuan disediakan tim FE/BE; endpoint tidak dikarang).
- Tabel Validasi Edit (TC | Field | Nilai uji | Pesan error di bawah field):
  - TC-143 | Client Code | TKM-002 (Client Code C-02, Pre-setup, hanya diketik) | Client code already exists
  - TC-144 | Company Name | (kosong) | Company name must not be empty
  - TC-145 | Company Name | A×121 | Max. 120 characters
  - TC-146 | PIC Email | pic@ | Enter a valid email address
  - TC-147 | Address | A×361 | Max. 360 characters
  - TC-148 | Postal Code | 12AB5 | Postal code contains invalid characters
  - TC-149 | Company Name | pt teknologi maju (Company Name C-02, Pre-setup, hanya diketik) | Company name already exists
  - TC-524 | Company Email | 109×`a` + `@example.com` (121 karakter) | Max. 120 characters
  - TC-524 | PIC Name | A×121 | Max. 120 characters
  - TC-524 | PIC Email | 109×`a` + `@example.com` (121 karakter) | Max. 120 characters
  - TC-524 | Website | A×121 | Max. 120 characters
  - TC-524 | Fax | 121×`1` | Max. 120 characters
  - TC-525 | Client Code | ABCDEFGHIJKLMNOP (16 karakter) | Max. 15 characters
  - TC-525 | PIC Phone | 1234567890123456 | Max. 15 characters
  - TC-525 | Postal Code | 1234567890123456 | Max. 15 characters
  - TC-526 | PIC Phone | 123 | Min. 4 characters
  - TC-529 | Client Code | AB@#12 | Client code contains invalid characters
  - TC-529 | PIC Phone | 08ab1234 | PIC phone contains invalid characters
  - TC-537 | Company Name | dua spasi + PT TEKNOLOGI MAJU + dua spasi | Company name already exists
- Kasus berurutan khusus: TC-142 (Client Code dikosongkan), TC-536 (Client Code huruf kecil), dan TC-523 (Country diganti, State lalu City wajib).
- Cleanup: hook `after` menghapus kedua Client seed lewat API.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

### TC-142: Client Code wajib saat Edit

1. Ketik Search `PT Sejahtera Abadi {runId}-067`, tekan Enter
2. Buka `⋯` baris `PT Sejahtera Abadi {runId}-067` lalu klik `Edit`
3. Kosongkan field Client Code
4. Klik `[Save]`
5. Verifikasi pesan error "Client code must not be empty"
6. Verifikasi field Client Code tidak terisi otomatis
7. Verifikasi popup tetap terbuka
8. Ganti isi Client Code dengan `SJA-{r6}`

### Tabel Validasi Edit

9. Untuk setiap baris tabel Validasi Edit di Prerequisites, lakukan langkah 10 sampai 15
10. Ganti isi field baris tabel dengan nilai uji (nilai "(kosong)" berarti field dikosongkan)
11. Klik `[Save]`
12. Verifikasi pesan error inline di bawah field sama dengan kolom Pesan error baris tabel
13. Verifikasi popup tetap terbuka
14. Verifikasi tidak ada toast
15. Kembalikan field ke nilai tersimpan

### TC-536: Client Code huruf kecil diubah otomatis menjadi kapital

16. Ketik Client Code `tkm-002` tanpa memindahkan fokus dari field
17. Verifikasi field Client Code menampilkan "TKM-002"
18. Verifikasi pesan error "Client code already exists" muncul langsung
19. Ganti isi Client Code dengan `SJA-{r6}`

### TC-523: State dan City wajib setelah Country diganti

20. Ganti Country menjadi "Malaysia" (State dan City ter-reset)
21. Klik `[Save]`
22. Verifikasi State menampilkan pesan error "State must not be empty"
23. Pilih State "Selangor"
24. Klik `[Save]`
25. Verifikasi City menampilkan pesan error "City must not be empty"
26. Verifikasi popup tetap terbuka
27. Verifikasi tidak ada toast
28. Klik `[✕]` di header popup
29. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]` tampil
30. Klik `[Leave]`

### Data tidak berubah

31. Klik Company Name `PT Sejahtera Abadi {runId}-067` untuk membuka Detail
32. Verifikasi Company Name "PT Sejahtera Abadi {runId}-067", Client Code "SJA-{r6}", dan PIC Email "pic.old@example.com" tidak berubah
33. Klik breadcrumb "Client" untuk kembali ke List

### TC-944: Client Code dengan spasi akhir ditolak whitelist

34. Ketik Search `PT Menteng Jeda {runId}-067`, tekan Enter
35. Buka `⋯` baris `PT Menteng Jeda {runId}-067` lalu klik `Edit`
36. Klik di ujung kanan field Client Code lalu ketik satu spasi
37. Tunggu 1 detik
38. Verifikasi pesan error inline di bawah Client Code: "Client code contains invalid characters"
39. Klik `[Save]`
40. Verifikasi popup tetap terbuka
41. Verifikasi tidak ada toast sukses "Success, client has been updated."
42. Klik `[✕]` di header popup
43. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]` tampil
44. Klik `[Leave]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Alasan di atas 35 langkah (setara sekitar 130 langkah setelah ekspansi tabel): satu popup Edit pada Client seed, satu role, satu kelas (validasi diblokir); parameter di tabel Prerequisites, langkah 10 sampai 15 diulang untuk 19 baris (butir 8b-7); tiap baris berdiri sendiri.
- Langkah penghubung (S-03): pengembalian field ke nilai tersimpan (langkah 15), penutup form dirty (S-08), Detail dan breadcrumb "Client" untuk membuktikan data tidak berubah. Pesan error diasersi sesudah `[Save]` pada semua baris (TC-524, TC-525, TC-529, TC-536 menyebut "langsung saat nilai diisi"; pesan yang sama tetap tampil sesudah `[Save]`).
- Nilai Pre-setup C-02 hanya diketik sebagai sumber duplikat; tidak ada aksi tulis ke baris Pre-setup (catatan S-06).
- Temuan untuk QA:
  - TC-144 sampai TC-148 Expected "data tidak berubah" tidak punya langkah observasi sendiri; spec membuktikannya sekali lewat Detail sesudah semua baris.
  - TC-523 menyebut Country "Malaysia" dan State "Selangor" tanpa menyebut City yang dipilih sesudahnya; spec berhenti sesudah error City.
