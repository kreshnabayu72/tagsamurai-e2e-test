---
id: TC-AC-CS-E2E-136-defense-in-depth-requester-dan-scope-distributor
title: "Defense-in-Depth: Requester dan Scope Distributor"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-CS-507
  - TC-AC-CS-511
  - TC-AC-CS-510
  - TC-AC-CS-508
  - TC-AC-CS-509
  - TC-AC-CS-512
coverage:
  web: automated
---

# Defense-in-Depth: Requester dan Scope Distributor

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Create-Only Distributor (Pre-setup #6) `createOnlySub_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`, tanpa Delete dan tanpa Manage active client), password `Spectra.env.AC_SUB_CREATE_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Akun ganti akun di tengah spec (Test Steps memuat langkah Logout dan login eksplisit):

| Urutan | Pre-setup | Email | Peran | Env password |
|---|---|---|---|---|
| 2 | #12 | `createOnlyPartnerSub_automated_{namaCompany}@qwertysystem.net` (`Rina Pratama`) | Create-Only, Partner CV Karya Mandiri (requester original record Canceled) | `Spectra.env.AC_SUB_PARTNER_CREATE_PASSWORD` |
| 3 | #9 | `totalControlDistSub_automated_{namaCompany}@qwertysystem.net` (`Eko Saputra`) | Total Control Distributor PT Maju Bersama | `Spectra.env.AC_SUB_DIST_TC_PASSWORD` |

- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- State global: toggle Require Approval for Allocation PT Maju Bersama diatur ON oleh fixture backend yang disediakan tim FE/BE di hook `before` (pengajuan `Fajar Nugroho` berstatus Waiting for Approval) dan dipulihkan di hook `after` (S-06, pengecualian 2026-10-30). Suite berjalan serial.
- Kemampuan teknis (disediakan tim FE/BE): klien HTTP atau fixture BE yang mengirim request dengan token sesi aktor (login API password, token tidak dihitung sebagai sesi web); membaca status, jumlah record, dan entri log sebagai state data. Aksi yang dikirim hanya yang dinamai TC; path dan body tidak tertulis di TC, PRD, atau LLD sehingga disediakan tim FE/BE tanpa endpoint karangan (S-13, bagian 8b butir 1).
- Data milik spec, dibuat lewat API di hook `before` dan dibersihkan di hook `after` (S-06, S-12; semua request yang diuji ditolak sehingga tidak ada perubahan data; bersuffix `+{runId}-136`); jumlah record dan entri log dicatat sebagai baseline sebelum langkah pertama:
  1. TC-AC-CS-507: term Active `T507A` milik Plan Owner PT Maju Bersama (setara `SUBS-20250815-00001`, #69) dan term Active `T507B` plan Free milik Client binaan CV Karya Mandiri (Plan Owner lain, di luar scope WRITE; setara #74).
  2. TC-AC-CS-508 dan 509: pengajuan Waiting for Approval `W509` milik requester `Fajar Nugroho` (Plan Owner PT Maju Bersama; setara #49), dan record `X509` berstatus Canceled yang requester originalnya `Rina Pratama` (setara `SUBS-20260805-00001`, #56).
  3. TC-AC-CS-510: record Canceled `X509` yang sama sebagai sumber Resubmit (requester lain dari `Fajar Nugroho`).
  4. TC-AC-CS-512: Client `C512` binaan langsung CV Karya Mandiri (Partner), bukan binaan langsung Distributor (setara `Bengkel Maju Jaya`, #30).
- Hook suite (lihat `suite.md`): `beforeEach` membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09; flag Guided Tooltip diatur `seen`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-507: Cancel Subscription langsung tanpa Delete atau di luar scope WRITE ditolak

1. Kirim POST Cancel Subscription pada term `T507A` dengan token sesi aktor `Fajar Nugroho`
2. Verifikasi respons server menolak karena aktor tanpa capability Delete
3. Kirim POST Cancel Subscription pada term Active `T507B` dengan token sesi aktor `Fajar Nugroho`
4. Verifikasi respons server menolak karena term di luar scope WRITE
5. Verifikasi status term `T507A` dan `T507B` tidak berubah (Active)

### TC-AC-CS-511: Pembuatan Client baru lewat Add Subscription tanpa Manage active client ditolak

6. Kirim POST Add Subscription dengan data `[+ New Client]` dengan token sesi aktor `Fajar Nugroho`
7. Verifikasi respons server menolak
8. Verifikasi tidak ada Client, Default User, maupun term yang dibuat

### TC-AC-CS-510: Resubmit langsung oleh aktor bukan requester original ditolak

9. Kirim POST Resubmit dari record Canceled `X509` dengan token sesi aktor `Fajar Nugroho`
10. Verifikasi respons server menolak
11. Verifikasi tidak ada record baru

### TC-AC-CS-508: Cancel Request langsung oleh aktor bukan requester ditolak

12. Logout
13. Login sebagai Create-Only Partner `Rina Pratama`
14. Kirim POST Cancel Request pada pengajuan `W509` dengan token sesi aktor `Rina Pratama`
15. Verifikasi respons server menolak
16. Verifikasi status pengajuan `W509` tetap Waiting for Approval

### TC-AC-CS-509: Edit langsung oleh aktor bukan requester atau pada status tidak valid ditolak

17. Kirim PUT Edit Duration pada pengajuan `W509` (aktor bukan requester)
18. Verifikasi respons server menolak karena aktor bukan requester
19. Kirim PUT Edit Duration yang sama pada record Canceled `X509` (requester original aktor)
20. Verifikasi respons server menolak karena status Canceled tidak dapat di-Edit
21. Verifikasi data `W509` dan `X509` tampil tidak berubah
22. Verifikasi tidak ada entri log baru pada `W509` dan `X509` (jumlah sama dengan baseline)

### TC-AC-CS-512: Add Subscription langsung untuk Client di luar binaan langsung ditolak

23. Logout
24. Login sebagai Total Control Distributor `Eko Saputra`
25. Kirim POST Add Subscription untuk Client `C512` dengan token sesi aktor `Eko Saputra`
26. Verifikasi respons server menolak karena scope Create exact match
27. Verifikasi tidak ada term baru pada Client `C512`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- K-1: TC kelas a (defense-in-depth) dengan Expected berupa respons API tetap masuk spec FE+BE walau tumpang tindih dengan `tc-license-allocation-subscription-backend.md`; asersi hanya respons server dan state data (bagian 8b butir 1), tanpa perilaku FE.
- Urutan TC berbeda dari kolom `sourceTc` (507, 511, 510, 508, 509, 512) hanya mengikuti kelompok akun: Fajar Nugroho (507, 511, 510), Rina Pratama (508, 509), Eko Saputra (512), sehingga hanya terjadi dua pergantian akun (S-07).
- Langkah penghubung (S-03): langkah 12 dan 23 (Logout sebagai bagian ganti akun).
- Temuan untuk QA:
  - TC-AC-CS-507 sampai 512 Expected tidak menyebut status HTTP maupun kode error; spec mengasersi penolakan dengan alasan yang diberikan TC (S-02).
  - TC-AC-CS-509 Expected b ("tidak ada entri log baru") tidak menyebut surface log; spec memakai jumlah entri log record yang dibaca fixture BE.
  - TC-AC-CS-508 dan 509 memakai pengajuan `SUBS-20260819-00001` yang sama dengan TC lain; spec memakai record milik spec (S-06).
  - TC-AC-CS-511 tidak menyebut body request `[+ New Client]` (Client, Default User); body disediakan tim FE/BE.
