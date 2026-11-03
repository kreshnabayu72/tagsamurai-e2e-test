---
id: TC-AC-ACC-E2E-044-create-duplikat-ditolak-dan-spasi-client-code-af
title: "Validasi Create: Duplikat Company Name, Client Code, dan Email Default User Ditolak (Active-Full)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-113
  - TC-AC-ACC-114
  - TC-AC-ACC-115
  - TC-AC-ACC-942
  - TC-AC-ACC-118
  - TC-AC-ACC-498
coverage:
  web: automated
---

# Validasi Create: Duplikat Company Name, Client Code, dan Email Default User Ditolak (Active-Full)

## Prerequisites

- Mode: FE+BE. Tidak ada Client yang berhasil dibuat; submit diblokir.
- Akun aktor: Active-Full (A-15) `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD`. Login akun Active-Full di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya.
- Sumber duplikat (data Pre-setup yang hanya dibaca dan hanya diketik sebagai nilai uji, tidak diubah): Company Name C-01 `PT Sejahtera Abadi`, Client Code C-01 `SJA-001`, Email Default User A-16 `clientDefaultUser_automated_ptSejahteraAbadi@qwertysystem.net`.
- Data valid Create (kecuali bila kasus menyebut lain): PIC Name `Rina Kartika`; PIC Email `rina.kartika@qwertysystem.net`; Address `Jl. Sudirman No. 10`; Country/State/City `Indonesia`/`DKI Jakarta`/`Jakarta Selatan`; Postal Code `12190`; Default User First Name, Last Name, Email (`<nama>+{runId}-044@qwertysystem.net`, unik per run), Division `Finance`; Position kosong; Select Group `Area Jakarta` bila Partner kosong. Company Name valid `PT Duplikat Uji {runId}-044`.
- Cleanup: tidak ada data yang perlu dihapus.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

1. Klik `[+ New Client]`

### TC-113: Company Name duplikat ditolak langsung

2. Ketik Company Name `PT Sejahtera Abadi` tanpa memindahkan fokus
3. Tunggu sekitar 500 ms
4. Verifikasi pesan error "Company name already exists" muncul langsung tanpa menunggu blur
5. Isi PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; pilih Group "Area Jakarta"
6. Klik `[Submit]`
7. Verifikasi popup tetap terbuka
8. Verifikasi tidak ada toast sukses "Success, client has been created."

### TC-114: Duplikat beda huruf besar-kecil dan spasi tepi

9. Ganti isi Company Name dengan `  pt sejahtera abadi  ` (huruf kecil, dua spasi di tiap tepi) tanpa memindahkan fokus
10. Tunggu 1 detik
11. Verifikasi pesan error inline di bawah Company Name: "Company name already exists"
12. Ganti isi Company Name dengan `PT Duplikat Uji {runId}-044`

### TC-115: Client Code duplikat

13. Ketik Client Code `sja-001`
14. Verifikasi field Client Code menampilkan `SJA-001` (otomatis kapital)
15. Verifikasi pesan error "Client code already exists"

### TC-942: Client Code dengan spasi awal atau akhir ditolak whitelist

16. Ganti isi Client Code dengan ` SPC-901` (satu spasi di awal)
17. Tunggu 1 detik
18. Verifikasi pesan error inline di bawah Client Code: "Client code contains invalid characters"
19. Klik `[Submit]`
20. Verifikasi popup tetap terbuka
21. Verifikasi tidak ada toast sukses "Success, client has been created."
22. Kosongkan field Client Code lalu ketik `SPC-902 ` (satu spasi di akhir)
23. Tunggu 1 detik
24. Verifikasi pesan error inline di bawah Client Code: "Client code contains invalid characters"
25. Klik `[Submit]`
26. Verifikasi popup tetap terbuka
27. Verifikasi tidak ada toast sukses "Success, client has been created."
28. Kosongkan field Client Code

### TC-118: Email Default User milik user Client lain ditolak

29. Ganti isi Email Default User dengan `clientDefaultUser_automated_ptSejahteraAbadi@qwertysystem.net` tanpa memindahkan fokus
30. Tunggu sekitar 500 ms
31. Verifikasi pesan error "Email already exists" muncul langsung tanpa menunggu blur

### TC-498: Email duplikat beda huruf besar-kecil dan spasi tepi

32. Ganti isi Email Default User dengan `  ClientDefaultUser_Automated_PtSejahteraAbadi@QWERTYSYSTEM.NET  ` tanpa memindahkan fokus
33. Tunggu 1 detik
34. Verifikasi pesan error inline di bawah Email: "Email already exists" (tanpa pindah fokus)
35. Klik `[Submit]`
36. Verifikasi popup tetap terbuka
37. Verifikasi tidak ada toast sukses "Success, client has been created."

### Penutup

38. Klik `[✕]` di header popup
39. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]` tampil
40. Klik `[Leave]`
41. Ketik Search `PT Duplikat Uji {runId}-044`, tekan Enter
42. Verifikasi tidak ada Client "PT Duplikat Uji {runId}-044" yang dibuat (empty state "No results found")

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Alasan di atas 35 langkah (sekitar 45 langkah): satu form Create, satu role, satu kelas (duplikat diblokir, tanpa data tercipta), satu pembukaan form dipakai berulang (prinsip 13).
- Langkah penghubung (S-03): pengisian field valid sebelum `[Submit]`, penggantian Company Name ke nilai unik, pengosongan Client Code, dan penutup form dirty (S-08).
- Nilai Pre-setup C-01 dipakai hanya sebagai nilai yang diketik untuk memicu pesan duplikat (tidak ada aksi tulis ke baris Pre-setup; catatan S-06). "Tidak ada Client dibuat" dibuktikan satu kali di akhir dengan Search nama unik (empty state "No results found" sebagai anchor).
- Temuan untuk QA:
  - TC-113 Expected butir b ("Submit tidak membuat Client") tidak punya langkah `[Submit]` di TC; spec menambah langkah `[Submit]` dengan field valid agar butir b teramati.
  - TC-115 dan TC-118 tidak menyebut penutupan form; spec memakai penutup `✕`, dialog, `[Leave]` di akhir spec.
