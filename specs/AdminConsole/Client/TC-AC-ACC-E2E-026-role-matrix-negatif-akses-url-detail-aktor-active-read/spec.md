---
id: TC-AC-ACC-E2E-026-role-matrix-negatif-akses-url-detail-aktor-active-read
title: "Role Matrix Negatif: Akses URL Detail Client oleh Aktor Active-Read (403 Role Penaung dan 404 Netral di Luar Scope)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-61
  - TC-AC-ACC-564
  - TC-AC-ACC-565
  - TC-AC-ACC-954
  - TC-AC-ACC-965
  - TC-AC-ACC-951
coverage:
  web: automated
---

# Role Matrix Negatif: Akses URL Detail Client oleh Aktor Active-Read (403 Role Penaung dan 404 Netral di Luar Scope)

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-04 | Active-Read (Manage active client: Read, exact-match Area Jakarta) | `activeReadJakarta_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_ACTIVE_READ_PASSWORD` |

- Login di hook `before` spec ini (Active-Read, A-04); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Fixture A3 residen `C-ROL-5` `PT Suspend Menteng` (Suspended, Direct, Group `Cabang Menteng`), `C-ROL-6` `PT Arsip Menteng` (Archived, Direct, Group `Cabang Menteng`), `C-ROL-7` `PT Regional Barat` (Direct, Group `Regional Barat`), dan Pre-setup `C-09` `PT Baru Daftar` (Group `Cabang Menteng`), `C-12` `PT Timur Perkasa`, `C-04` `PT Karya Abadi` hanya dibaca. Assignment aktor A-04 hanya pada node `Area Jakarta` (exact-match, tanpa `Cabang Menteng`).
- ID Client untuk URL Detail (UUID opaque) semua Client di atas dan ID tidak terdaftar `3f9a1c2e-7b44-4d0e-9a51-6c2d8e1f0b77` diambil dari keluaran skrip seed atau respons API; kemampuan membaca ID disediakan tim FE/BE.
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).

## Test Steps

### TC-AC-ACC-61: Detail Client di luar scope group atau tidak ada: 404 netral

1. Buka URL Detail dengan ID Client `PT Timur Perkasa` (Area Surabaya) langsung
2. Verifikasi toast netral `This client is no longer available.`
3. Verifikasi halaman kembali ke List
4. Verifikasi data Client `PT Timur Perkasa` tidak tampil
5. Tunggu toast lama hilang otomatis
6. Buka URL Detail dengan ID Client yang tidak terdaftar langsung
7. Verifikasi toast netral `This client is no longer available.`
8. Verifikasi halaman kembali ke List
9. Verifikasi data Client tidak tampil
10. Tunggu toast lama hilang otomatis

### TC-AC-ACC-564: Detail Client di descendant dari node assignment exact-match diperlakukan seperti tidak ada

11. Buka URL Detail dengan ID Client `PT Sejahtera Abadi` langsung
12. Verifikasi halaman Detail `PT Sejahtera Abadi` terbuka
13. Buka URL Detail dengan ID Client `PT Baru Daftar` langsung
14. Verifikasi toast netral `This client is no longer available.`
15. Verifikasi halaman kembali ke List
16. Verifikasi data `PT Baru Daftar` tidak tampil
17. Tunggu toast lama hilang otomatis

### TC-AC-ACC-565: Detail Client di ancestor dari node assignment exact-match diperlakukan seperti tidak ada

18. Buka URL Detail dengan ID Client `PT Sejahtera Abadi` langsung
19. Verifikasi halaman Detail `PT Sejahtera Abadi` terbuka
20. Buka URL Detail dengan ID Client `PT Regional Barat` langsung
21. Verifikasi toast netral `This client is no longer available.`
22. Verifikasi halaman kembali ke List
23. Verifikasi data `PT Regional Barat` tidak tampil
24. Tunggu toast lama hilang otomatis

### TC-AC-ACC-954: Aktor Manage active client berhak membuka Detail Client Suspended di luar scope group: 404 netral

25. Klik sub-tab `Suspended`
26. Ketik Search `PT Wahana Nusantara`, tekan Enter
27. Klik Company Name `PT Wahana Nusantara` untuk membuka Detail
28. Verifikasi Detail `PT Wahana Nusantara` terbuka
29. Buka URL Detail dengan ID Client `PT Suspend Menteng` (Suspended) langsung
30. Verifikasi toast netral `This client is no longer available.`
31. Verifikasi halaman kembali ke List
32. Verifikasi data Client `PT Suspend Menteng` tidak tampil dan tidak ada petunjuk bahwa Client berada di luar scope
33. Tunggu toast lama hilang otomatis

### TC-AC-ACC-965: Detail Client Archived di luar scope group oleh aktor Manage active client saja: 404 netral

34. Klik sub-tab `Active`
35. Ketik Search `PT Sejahtera Abadi`, tekan Enter
36. Klik Company Name `PT Sejahtera Abadi` untuk membuka Detail
37. Verifikasi Detail `PT Sejahtera Abadi` terbuka
38. Buka URL Detail dengan ID Client `PT Arsip Menteng` (Archived, Group `Cabang Menteng`) langsung
39. Verifikasi toast netral `This client is no longer available.` lalu halaman kembali ke List
40. Verifikasi data `PT Arsip Menteng` tidak tampil (Client di luar scope diperlakukan seperti tidak ada, bukan 403 walau role yang menaungi status Archived tidak dimiliki)
41. Tunggu toast lama hilang otomatis

### TC-AC-ACC-951: Akses langsung URL Detail Client Archived dalam scope oleh aktor Manage active client saja: 403

42. Klik sub-tab `Active`
43. Ketik Search `PT Sejahtera Abadi`, tekan Enter
44. Klik Company Name `PT Sejahtera Abadi` untuk membuka Detail
45. Verifikasi Detail `PT Sejahtera Abadi` terbuka
46. Buka URL Detail dengan ID Client `PT Karya Abadi` (Archived) langsung
47. Verifikasi halaman no-access tampil (tanpa redirect ke halaman lain yang bukan no-access)
48. Verifikasi tidak ada toast error
49. Verifikasi data Client `PT Karya Abadi` tidak tampil

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 5, 10, 17, 24, 26, 33, 34, 41, 42. Tanpa awalan `Verifikasi`; menyiapkan, menutup, atau membersihkan state untuk blok berikutnya, atau mencari baris target lewat Search (R-16).
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- Penyimpangan urutan (S-05): TC-AC-ACC-61, 564, 565, 954, 965, 951 (semula 61, 564, 565, 951, 954, 965); blok no-access (TC-AC-ACC-951) di akhir karena hasilnya halaman no-access tanpa toast (D-015), berbeda dari blok 404 netral yang memakai toast, sehingga asersi tidak tercampur.
- Keputusan pemilik (klik, 2026-11-02): spec mengikuti `docs/spec-decisions.md` D-015 (menggantikan pilihan Q1 sebelumnya). Akses URL langsung tanpa capability diarahkan ke halaman no-access, tanpa toast `You don't have permission to do this.`, berlaku app-wide. Teks atau elemen pasti halaman no-access belum tercatat (spec Brand TC-GS-BRAND-E2E-010 dan D-015 hanya menyebut "halaman no-access tampil"); spec mengasersi dengan cara yang sama: halaman no-access tampil sebagai anchor positif, lalu tidak ada toast dan tidak ada data Client termuat. Toast untuk aksi atau request yang ditolak di halaman yang boleh dibuka tidak berubah.
- Asersi `Verifikasi` data Client tidak tampil memakai halaman yang termuat (toast atau List tampil) sebagai anchor; asersi toast netral memakai langkah "Tunggu toast lama hilang otomatis" di antara blok supaya toast tidak tertukar (R-12).
- Pembagian TC lintas spec: akses URL untuk aktor Archived-Read (TC-AC-ACC-952, 953) di spec 027; aktor tanpa capability di spec 025; Distributor dan Partner di spec 016 dan 018.
- Ukuran spec (49 langkah, melewati sekitar 35 langkah): satu akun (Active-Read), satu topik (akses URL Detail), tanpa aksi tulis, dan tiap blok TC dimulai dengan membuka URL eksplisit sehingga kegagalan satu blok tidak menghilangkan makna blok lain; langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01).
- Temuan untuk QA:
  - Sudah selaras (2026-11-03, temuan T-1 e2e-audit): Expected TC-AC-ACC-951 dan PRD client §9.3 (butir 1 dan 3, EC-80, EC-88) kini menyebut halaman no-access tampil tanpa toast error untuk akses URL langsung tanpa capability, sama dengan D-015. Spec mengasersi halaman no-access tampil tanpa toast dan tanpa data Client. Teks atau elemen halaman no-access belum diketahui; script memakai asersi yang sama dengan spec Brand.
  - TC-AC-ACC-61, 564, 565, 954, 965: kata "kembali ke List" tidak menyebut sub-tab yang dituju; spec mengasersi halaman List tampil.
  - TC-AC-ACC-954: langkah 3 TC menyebut aktor dapat membuka Detail Suspended dalam scope (`PT Wahana Nusantara`); spec mengikuti urutan TC.
