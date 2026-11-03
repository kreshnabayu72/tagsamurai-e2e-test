---
id: TC-AC-ACC-E2E-025-role-matrix-negatif-menu-client-tersembunyi-dan-url-ditolak
title: "Role Matrix Negatif: Menu Client Tersembunyi dan Akses URL Langsung Ditolak tanpa Capability"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-42
  - TC-AC-ACC-453
  - TC-AC-ACC-43
  - TC-AC-ACC-60
  - TC-AC-ACC-44
coverage:
  web: automated
---

# Role Matrix Negatif: Menu Client Tersembunyi dan Akses URL Langsung Ditolak tanpa Capability

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-16 | Client Default User (PT Sejahtera Abadi) | `clientDefaultUser_automated_ptSejahteraAbadi@qwertysystem.net` | `Spectra.env.AC_CLIENT_DEFAULT_USER_PASSWORD` |
| A-12 | Tanpa-Capability-Client (tidak punya Manage active/archived client/Manage allocation) | `noClientCapability_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_NO_CAPABILITY_PASSWORD` |
| A-11 | Allocation-Only (Manage allocation: Read, tanpa Manage active/archived client) | `allocationOnly_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_ALLOCATION_ONLY_PASSWORD` |

- Login di hook `before` spec ini (Client Default User, A-16); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Aktor tidak punya akses List Client, sehingga layar awal List dari hook `beforeEach` suite tidak berlaku; langkah pertama tiap blok role berada di beranda produk (precondition TC).
- ID Client untuk URL Detail (UUID opaque) `PT Timur Perkasa` (C-12; Active), `PT Sejahtera Abadi` (C-01; Active), dan `PT Karya Abadi` (C-04; Archived) diambil dari keluaran skrip seed atau respons API; ID tidak terdaftar `3f9a1c2e-7b44-4d0e-9a51-6c2d8e1f0b77`. Kemampuan membaca ID disediakan tim FE/BE.
- Perilaku akses URL langsung (diarahkan ke halaman no-access tanpa toast) mengikuti D-015 dan keputusan user 2026-11-02 (lihat Notes).
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).

## Test Steps

### TC-AC-ACC-42: Aktor entitas Client tidak punya akses menu Client

1. Cari menu Client di navigasi Admin Console (beranda produk Client Default User)
2. Verifikasi sedikitnya satu item menu lain tampil di navigasi
3. Verifikasi menu `Client` tidak tersedia (Hidden)
4. Buka URL Admin Console > Client langsung
5. Verifikasi halaman no-access tampil (tanpa redirect ke halaman lain yang bukan no-access)
6. Verifikasi tidak ada toast error `You don't have permission to do this.`
7. Verifikasi data Client tidak tampil

### TC-AC-ACC-453: Tenant isolation: Default User tenant Client tidak dapat mengakses Admin Console

8. Coba buka Admin Console > Client langsung
9. Verifikasi akses ditolak: halaman no-access tampil, halaman List Client tidak termuat dan data Client tidak tampil
10. Logout dari akun Client Default User
11. Login sebagai Tanpa-Capability-Client (A-12)

### TC-AC-ACC-43: Aktor tanpa capability Client tidak melihat menu dan ditolak akses langsung

12. Lihat sidebar Admin Console
13. Verifikasi sedikitnya satu item menu lain tampil di sidebar
14. Verifikasi menu `Client` tidak tampil
15. Buka URL Admin Console > Client langsung
16. Verifikasi halaman no-access tampil (tanpa redirect ke halaman lain yang bukan no-access)
17. Verifikasi tidak ada toast error `You don't have permission to do this.`

### TC-AC-ACC-60: Akses langsung URL Detail Client oleh aktor tanpa Read: 403 untuk setiap ID

18. Buka URL Detail dengan ID Client `PT Timur Perkasa` (Active) langsung
19. Verifikasi halaman no-access tampil (tanpa redirect ke halaman lain yang bukan no-access)
20. Verifikasi tidak ada toast error `You don't have permission to do this.`
21. Verifikasi data Client `PT Timur Perkasa` tidak tampil
22. Buka URL Detail dengan ID Client `PT Sejahtera Abadi` (Active) langsung
23. Verifikasi halaman no-access tampil (tanpa redirect ke halaman lain yang bukan no-access)
24. Verifikasi tidak ada toast error `You don't have permission to do this.`
25. Verifikasi data Client `PT Sejahtera Abadi` tidak tampil
26. Buka URL Detail dengan ID Client `PT Karya Abadi` (Archived) langsung
27. Verifikasi halaman no-access tampil (tanpa redirect ke halaman lain yang bukan no-access)
28. Verifikasi tidak ada toast error `You don't have permission to do this.`
29. Verifikasi data Client `PT Karya Abadi` tidak tampil
30. Buka URL Detail dengan ID Client yang tidak terdaftar langsung
31. Verifikasi halaman no-access tampil (tanpa redirect ke halaman lain yang bukan no-access)
32. Verifikasi tidak ada toast error `You don't have permission to do this.`
33. Verifikasi data Client tidak tampil
34. Verifikasi halaman no-access untuk ID tidak terdaftar sama dengan halaman no-access untuk ketiga Client terdaftar, bukan toast netral `This client is no longer available.`
35. Logout dari akun Tanpa-Capability-Client
36. Login sebagai Allocation-Only (A-11)

### TC-AC-ACC-44: Aktor hanya Manage allocation tidak bisa masuk modul Client

37. Lihat sidebar Admin Console
38. Verifikasi sedikitnya satu item menu lain tampil di sidebar
39. Verifikasi menu `Client` tidak tampil (role Manage allocation tidak memberi akses List dan Detail Client)
40. Buka URL Admin Console > Client langsung
41. Verifikasi halaman no-access tampil (tanpa redirect ke halaman lain yang bukan no-access)
42. Verifikasi tidak ada toast error `You don't have permission to do this.`
43. Buka Admin Console > Client Subscription
44. Verifikasi Client Subscription menampilkan tabel client beserta subscription-nya

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 10, 11, 35, 36. Tanpa awalan `Verifikasi`; menyiapkan, menutup, atau membersihkan state untuk blok berikutnya, atau mencari baris target lewat Search (R-16).
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- Penyimpangan urutan (S-05): TC-AC-ACC-42, 453, 43, 60, 44 (semula 42, 43, 44, 60, 453); TC-AC-ACC-42 dan 453 memakai akun Client Default User sehingga dikelompokkan bersama, lalu 43 dan 60 (Tanpa-Capability-Client), lalu 44 (Allocation-Only), supaya jumlah ganti akun minimal.
- Keputusan pemilik (klik, 2026-11-02): spec mengikuti `docs/spec-decisions.md` D-015 (menggantikan pilihan Q1 sebelumnya). Akses URL langsung tanpa capability diarahkan ke halaman no-access, tanpa toast `You don't have permission to do this.`, berlaku app-wide. Teks atau elemen pasti halaman no-access belum tercatat (spec Brand TC-GS-BRAND-E2E-010 dan D-015 hanya menyebut "halaman no-access tampil"); spec mengasersi dengan cara yang sama: halaman no-access tampil sebagai anchor positif, lalu tidak ada toast dan tidak ada data Client termuat. Toast untuk aksi atau request yang ditolak di halaman yang boleh dibuka tidak berubah.
- Langkah tanpa menunggu toast: karena D-015 tidak memunculkan toast, langkah "Tunggu toast lama hilang otomatis" dihapus. Langkah ganti akun (Logout dan Login) adalah langkah eksplisit (S-07); login akun pertama (Client Default User, A-16) dilakukan hook `before`. Spec Role Matrix per blok role karena langkah tiap role berbeda (bagian 3a; ganti akun menuntut Step eksplisit).
- Asersi absence menu `Client` didahului `Verifikasi` item menu lain tampil di sidebar yang sama (bagian 8b butir 2); asersi `Verifikasi` tidak ada toast dan data Client tidak tampil memakai halaman no-access yang tampil sebagai anchor positif.
- Pembagian TC lintas spec: akses URL Detail aktor dengan capability tetapi di luar scope atau role penaung berbeda ada di spec 026 dan 027.
- Ukuran spec (44 langkah, melewati sekitar 35 langkah): Role Matrix per blok role (tiga role, langkah berbeda); tiap blok dimulai dengan langkah ganti akun eksplisit dan tidak bergantung pada hasil blok sebelumnya; langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01) dan TC-AC-ACC-60 mengulang pola URL untuk empat ID dengan parameter tertera tiap langkah.
- Temuan untuk QA:
  - Selisih dengan D-015 dan keputusan user 2026-11-02: Expected TC-AC-ACC-42, 43, 44, 60 menyebut toast `You don't have permission to do this.` tanpa redirect untuk akses URL langsung tanpa capability (juga PRD client §9.3); TC tidak diubah. Spec mengasersi halaman no-access tampil tanpa toast dan tanpa data Client (D-015). QA perlu menyelaraskan Expected TC dan PRD §9.3. Teks atau elemen halaman no-access belum diketahui; script memakai asersi yang sama dengan spec Brand.
  - TC-AC-ACC-453: Expected hanya "Akses ditolak" tanpa bentuk penolakan (toast, redirect, atau halaman); spec mengasersi List tidak termuat dan data Client tidak tampil, bukan bentuk tertentu. TC-453 duplikat langkah TC-42 butir 2.
  - TC-AC-ACC-42, 43, 44: Expected "Menu Client Hidden" tidak menyebut item menu pembanding; spec memakai anchor "sedikitnya satu item menu lain" (bagian 8b butir 2). Bila beranda produk Client Default User tidak menampilkan navigasi Admin Console, QA perlu menyebut anchor lain.
  - TC-AC-ACC-44: Expected butir b menyebut "List/Detail" sedangkan langkah hanya membuka URL List; spec mengasersi URL List.
