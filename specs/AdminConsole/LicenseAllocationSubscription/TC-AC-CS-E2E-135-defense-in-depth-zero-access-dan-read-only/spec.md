---
id: TC-AC-CS-E2E-135-defense-in-depth-zero-access-dan-read-only
title: "Defense-in-Depth: Zero Access dan Read Only"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-CS-495
  - TC-AC-CS-496
  - TC-AC-CS-610
  - TC-AC-CS-497
  - TC-AC-CS-513
coverage:
  web: automated
---

# Defense-in-Depth: Zero Access dan Read Only

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Group C Zero Access Distributor (Pre-setup #18) `groupCZeroSub_automated_{namaCompany}@qwertysystem.net` (`Indra Kusuma`, Group Role Manage allocation pada Group lain, Zero Access pada Group C), password `Spectra.env.AC_SUB_GROUPC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Akun ganti akun di tengah spec (Test Steps memuat langkah Logout dan login eksplisit):

| Urutan | Pre-setup | Email | Peran | Env password |
|---|---|---|---|---|
| 2 | #3 | `readOnlySub_automated_{namaCompany}@qwertysystem.net` (`Rina Wijaya`) | Read Only, Principal PT ABC | `Spectra.env.AC_SUB_RO_PASSWORD` |
| 3 | #9 | `totalControlDistSub_automated_{namaCompany}@qwertysystem.net` (`Eko Saputra`) | Total Control Distributor PT Maju Bersama | `Spectra.env.AC_SUB_DIST_TC_PASSWORD` |

- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): klien HTTP atau fixture BE yang mengirim request dengan token sesi aktor (login API password, token tidak dihitung sebagai sesi web); membaca jumlah term, trial, dan entri log sebagai state data. Aksi yang dikirim hanya yang dinamai TC; path dan body tidak tertulis di TC, PRD, atau LLD sehingga disediakan tim FE/BE tanpa endpoint karangan (S-13, bagian 8b butir 1).
- Data milik spec, dibuat lewat API di hook `before` dan dibersihkan di hook `after` (S-06, S-12; semua request yang diuji ditolak sehingga tidak ada perubahan data); jumlah term dan trial dicatat sebagai baseline sebelum langkah pertama (bersuffix `+{runId}-135`):
  1. TC-AC-CS-495 dan 610: Client `Toko Group C+{runId}-135` (binaan langsung PT Maju Bersama pada group `Group C`, Zero Access bagi `Indra Kusuma`; setara Pre-setup #128) dengan term FAMS Active dan entri Subscription Log.
  2. TC-AC-CS-496: Client `Toko Group C+{runId}-135` yang sama sebagai target Add Subscription.
  3. TC-AC-CS-497: Client milik spec (binaan Principal) tanpa trial.
  4. TC-AC-CS-513: trial `T513A` FAMS Active (setara Pre-setup #60, Client binaan Principal dan PT Maju Bersama) dan trial `T513B` FAMS Growth Active milik Client binaan langsung CV Karya Mandiri (Partner), bukan binaan langsung PT Maju Bersama (setara Pre-setup #44 dan #74).
- Hook suite (lihat `suite.md`): `beforeEach` membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09; flag Guided Tooltip diatur `seen`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-495: Baca langsung term di scope Zero Access ditolak 403

1. Kirim GET detail term milik Client `Toko Group C+{runId}-135` dengan token sesi aktor `Indra Kusuma`
2. Verifikasi respons server berstatus 403
3. Verifikasi kode error `FORBIDDEN_GROUP_ACCESS`
4. Verifikasi tidak ada data term yang dikembalikan

### TC-AC-CS-496: Tulis langsung pada scope Zero Access ditolak 403

5. Kirim POST Add Subscription untuk Client `Toko Group C+{runId}-135` dengan token sesi aktor `Indra Kusuma`
6. Verifikasi respons server berstatus 403
7. Verifikasi kode error `FORBIDDEN_GROUP_ACCESS`
8. Verifikasi tidak ada term yang dibuat (jumlah term Client sama dengan baseline)

### TC-AC-CS-610: Buka langsung Subscription Log di scope Zero Access ditolak 403

9. Kirim GET Subscription Log term milik Client `Toko Group C+{runId}-135` dengan token sesi aktor `Indra Kusuma`
10. Verifikasi respons server berstatus 403
11. Verifikasi kode error `FORBIDDEN_GROUP_ACCESS` tampil pada body respons
12. Verifikasi tidak ada entri log yang dikembalikan
13. Ketik Search `Toko Group C+{runId}-135`, tekan Enter
14. Verifikasi empty state `No results found` tampil sehingga baris term Group C tidak tampil di List dan row action `Subscription Log` tidak tersedia di UI
15. Klik `(←)` pada kotak Search

### TC-AC-CS-497: Activate Trial langsung tanpa capability Create ditolak

16. Logout
17. Login sebagai Read Only `Rina Wijaya`
18. Kirim POST Activate Trial untuk Client milik spec dengan token sesi aktor `Rina Wijaya`
19. Verifikasi respons server menolak karena aktor tanpa izin Create
20. Verifikasi tidak ada trial dibuat (jumlah trial Client sama dengan baseline)

### TC-AC-CS-513: Convert langsung oleh aktor tanpa Create atau di luar scope WRITE ditolak

21. Kirim POST Convert pada trial `T513A` dengan token sesi aktor `Rina Wijaya`
22. Verifikasi respons server menolak karena aktor tanpa Create
23. Logout
24. Login sebagai Total Control Distributor `Eko Saputra`
25. Kirim POST Convert pada trial FAMS Growth Active `T513B` dengan token sesi aktor `Eko Saputra`
26. Verifikasi respons server menolak karena di luar scope WRITE (Client tidak di-bind langsung ke Distributor aktor)
27. Verifikasi trial `T513A` dan `T513B` tetap Active
28. Verifikasi tidak ada term paid baru

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- K-1: TC kelas a (defense-in-depth) dengan Expected berupa respons API tetap masuk spec FE+BE walau tumpang tindih dengan `tc-license-allocation-subscription-backend.md`; asersi hanya respons server dan state data (bagian 8b butir 1). Langkah 13 sampai 15 adalah satu-satunya asersi FE (TC-AC-CS-610 Expected c, List tidak menampilkan baris Group C).
- Langkah penghubung (S-03): langkah 13 (Search untuk menemukan baris target, R-16), langkah 15 (mengosongkan Search), dan langkah 16, 23 (Logout sebagai bagian ganti akun, S-07).
- Ganti akun eksplisit (langkah 16 sampai 17 dan 23 sampai 24) karena akun pertama login di hook `before`.
- Temuan untuk QA:
  - TC-AC-CS-497 Expected a ("aktor tanpa izin Create") dan TC-AC-CS-513 Expected a tidak menyebut status HTTP maupun kode error; spec mengasersi penolakan beserta alasannya sebagai klausa yang diberikan TC (S-02).
  - TC-AC-CS-513 langkah 2 menyebut Logout lalu login sebagai Distributor `Eko Saputra` untuk mengirim request langsung; spec mempertahankan ganti akun eksplisit sesuai TC.
  - TC-AC-CS-497 tidak menyebut Client target dan body request Activate Trial; spec memakai Client milik spec.
  - TC-AC-CS-495 dan 610 memakai baris Group C Pre-setup (#128); spec memakai Client milik spec pada group `Group C` (S-06), penempatan Client ke group disediakan tim FE/BE.
