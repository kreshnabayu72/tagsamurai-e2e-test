---
id: TC-AC-ACC-E2E-004-isi-sel-badge-produk-fams-sams-siem
title: "Isi Sel Badge Produk FAMS, SAMS, dan SIEM pada List Client"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-12
  - TC-AC-ACC-13
  - TC-AC-ACC-14
  - TC-AC-ACC-629
  - TC-AC-ACC-630
coverage:
  web: automated
---

# Isi Sel Badge Produk FAMS, SAMS, dan SIEM pada List Client

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-01 | Total Control (Principal) | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, A-01); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Fixture A3 residen `C-LIF-1` `PT Pengajuan Ditolak` (FAMS satu-satunya term Rejected, SAMS satu-satunya term Canceled, SIEM tidak pernah berlangganan) dan `C-LIF-2` `PT Riwayat Bergulir` (FAMS term lama Renewed dan term baru Active, SAMS term Active dengan term berikutnya Rejected, SIEM term Active dengan term berikutnya Canceled) hanya dibaca.
- Spec read-only; Search dibersihkan dalam spec.
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).

## Test Steps

### TC-AC-ACC-12: Sel FAMS/SAMS/SIEM menampilkan satu status terpadu dengan severity sesuai status

1. Ketik Search `PT Sejahtera Abadi`, tekan Enter
2. Lihat sel FAMS, SAMS, SIEM baris `PT Sejahtera Abadi`, lalu arahkan kursor ke tiap badge
3. Verifikasi FAMS, SAMS, dan SIEM `PT Sejahtera Abadi` adalah badge `Active` severity success
4. Verifikasi tiap produk hanya satu badge
5. Ganti isi kotak Search dengan `PT Teknologi Maju`, tekan Enter
6. Lihat sel FAMS, SAMS, SIEM baris `PT Teknologi Maju`, lalu arahkan kursor ke badge
7. Verifikasi FAMS `PT Teknologi Maju` adalah badge `Grace` severity warning
8. Verifikasi SAMS dan SIEM `PT Teknologi Maju` berupa teks sel `No Subscription` (bukan badge)
9. Verifikasi FAMS hanya satu badge
10. Ganti isi kotak Search dengan `PT Cahaya Baru`, tekan Enter
11. Lihat sel FAMS baris `PT Cahaya Baru`, lalu arahkan kursor ke badge
12. Verifikasi FAMS `PT Cahaya Baru` adalah badge `Waiting for Approval` severity warning
13. Verifikasi FAMS hanya satu badge
14. Ganti isi kotak Search dengan `PT Mulai Esok`, tekan Enter
15. Lihat sel FAMS baris `PT Mulai Esok`, lalu arahkan kursor ke badge
16. Verifikasi FAMS `PT Mulai Esok` adalah badge `Pending` severity warning
17. Verifikasi FAMS hanya satu badge
18. Klik `(←)` pada kotak Search

### TC-AC-ACC-13: Badge produk sub-tab Suspended dan status Expired

19. Klik sub-tab `Suspended`
20. Ketik Search `PT Wahana Nusantara`, tekan Enter
21. Lihat sel FAMS, SAMS, SIEM `PT Wahana Nusantara`
22. Verifikasi FAMS adalah badge `Expired` severity danger
23. Verifikasi SAMS adalah badge `Archive` severity dark
24. Verifikasi SIEM berupa teks sel `No Subscription`
25. Klik `(←)` pada kotak Search

### TC-AC-ACC-14: Badge produk sub-tab Archived: Archive, Purge, dan Deleted dengan severity dark

26. Klik sub-tab `Archived`
27. Ketik Search `PT Karya Abadi`, tekan Enter
28. Lihat sel FAMS, SAMS, SIEM `PT Karya Abadi`
29. Verifikasi FAMS, SAMS, dan SIEM `PT Karya Abadi` adalah badge `Archive` severity dark
30. Ganti isi kotak Search dengan `PT Lama Tak Berbayar`, tekan Enter
31. Lihat sel FAMS, SAMS, SIEM `PT Lama Tak Berbayar`, lalu arahkan kursor ke badge `Purge` dan `Deleted`
32. Verifikasi FAMS adalah badge `Purge` severity dark
33. Verifikasi SAMS adalah badge `Deleted` severity dark
34. Verifikasi SIEM berupa teks sel `No Subscription`
35. Verifikasi label teks membedakan `Purge` dan `Deleted` walau severity sama
36. Klik `(←)` pada kotak Search

### TC-AC-ACC-629: FAMS dan SAMS Client dengan term hanya Rejected atau Canceled menampilkan No Subscription

37. Klik sub-tab `Active`
38. Ketik Search `PT Pengajuan Ditolak`, tekan Enter
39. Lihat sel FAMS, SAMS, dan SIEM baris `PT Pengajuan Ditolak`
40. Verifikasi sel FAMS berisi teks `No Subscription` (teks sel, bukan badge)
41. Verifikasi label `Rejected` tidak tampil pada sel FAMS
42. Verifikasi sel SAMS berisi teks `No Subscription` (teks sel, bukan badge)
43. Verifikasi label `Canceled` tidak tampil pada sel SAMS
44. Verifikasi sel SIEM berisi teks `No Subscription`

### TC-AC-ACC-630: Sel produk Client dengan term Renewed di riwayat atau term berikutnya Rejected/Canceled menampilkan badge term Active

45. Klik `(←)` pada kotak Search
46. Klik sub-tab `Active`
47. Ketik Search `PT Riwayat Bergulir`, tekan Enter
48. Lihat sel FAMS, SAMS, dan SIEM baris `PT Riwayat Bergulir`
49. Verifikasi sel FAMS adalah badge `Active` severity success
50. Verifikasi badge `Renewed` tidak tampil pada sel FAMS
51. Verifikasi sel SAMS adalah badge `Active` severity success
52. Verifikasi badge `Rejected` tidak tampil pada sel SAMS
53. Verifikasi sel SIEM adalah badge `Active` severity success
54. Verifikasi badge `Canceled` tidak tampil pada sel SIEM
55. Verifikasi tiap produk hanya satu badge
56. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 5, 10, 14, 18, 20, 25, 27, 30, 36, 38, 45, 47, 56. Tanpa awalan `Verifikasi`; menyiapkan, menutup, atau membersihkan state untuk blok berikutnya, atau mencari baris target lewat Search (R-16).
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- Pembagian TC lintas spec: TC-AC-ACC-467 (badge produk Client Active dengan term terakhir Archive, aktor Active-Full) ada di spec 005.
- Asersi absence badge (`Renewed`, `Rejected`, `Canceled`, label `Rejected`/`Canceled`) memakai sel yang sama sebagai anchor positif: badge atau teks sel yang diharapkan tampil pada `Verifikasi` tepat sebelumnya (bagian 8b butir 2).
- TC-AC-ACC-12 langkah 'Hover tiap badge' tidak punya Expected sendiri; hover dituliskan sebagai aksi tanpa `Verifikasi`.
- Ukuran spec (56 langkah, melewati sekitar 35 langkah): satu dataset (badge produk List), tanpa aksi tulis, dan tiap blok TC berdiri sendiri (sub-tab dan Search dipilih eksplisit di awal blok) sehingga kegagalan satu blok tidak menghilangkan makna blok lain; langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01).
- Temuan untuk QA:
  - TC-AC-ACC-12: Expected butir e "Satu badge per produk per Client" tidak menyebut cara menghitung badge; spec mengasersi tiap produk hanya satu badge atau satu teks sel per Client yang dicari.
  - TC-AC-ACC-14: Expected butir c (label teks membedakan Purge dan Deleted) tidak menyebut label persisnya selain yang sudah diasersi pada butir b; spec mengasersi teks `Purge` dan `Deleted` pada sel yang berbeda.
