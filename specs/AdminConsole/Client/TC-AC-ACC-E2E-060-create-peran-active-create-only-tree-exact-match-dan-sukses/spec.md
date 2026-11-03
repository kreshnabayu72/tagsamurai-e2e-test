---
id: TC-AC-ACC-E2E-060-create-peran-active-create-only-tree-exact-match-dan-sukses
title: "Active-Create-Only: Tree Select Group Exact-Match dan Create Client Sampai Sukses"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-125
  - TC-AC-ACC-584
coverage:
  web: automated
---

# Active-Create-Only: Tree Select Group Exact-Match dan Create Client Sampai Sukses

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Active-Create-Only (A-05) `activeCreateJakarta_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_ACTIVE_CREATE_PASSWORD`. Login akun Active-Create-Only di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya.
- Assignment A-05 hanya pada node Area Jakarta (exact-match; ancestor greyed out, descendant hidden).
- Data valid Create (kecuali bila kasus menyebut lain): PIC Name `Rina Kartika`; PIC Email `rina.kartika@qwertysystem.net`; Address `Jl. Sudirman No. 10`; Country/State/City `Indonesia`/`DKI Jakarta`/`Jakarta Selatan`; Postal Code `12190`; Default User First Name, Last Name, Email (`<nama>+{runId}-060@qwertysystem.net`, unik per run), Division `Finance`; Position kosong; Select Group `Area Jakarta` bila Partner kosong. Default User untuk TC-584: `Dewi Anggraini`, Division `Operasional`, PIC Email `rina.kartika.cb+{runId}-060@qwertysystem.net`.
- Dataset Dinamis: `PT Pembuat Satu Kapabilitas {runId}-060`.
- Cleanup: hook `after` menghapus lewat API (soft-delete) Client yang dibuat atau di-seed spec ini, tanpa mengasumsikan setup berhasil penuh.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

### TC-125: Tree exact-match

1. Klik `[+ New Client]`
2. Biarkan field Partner kosong
3. Buka tree Select Group
4. Verifikasi "Area Jakarta" dapat dipilih
5. Verifikasi "Regional Barat" greyed out
6. Verifikasi "Cabang Menteng" tidak muncul (descendant hidden)
7. Klik node "Regional Barat"
8. Verifikasi tidak ada node terpilih
9. Verifikasi field Select Group tetap menampilkan placeholder "Select group"

### TC-584: Create sampai sukses

10. Isi Company Name `PT Pembuat Satu Kapabilitas {runId}-060`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; Default User Dewi Anggraini dengan Email `dewi.anggraini.cb+{runId}-060@qwertysystem.net`, Division `Operasional`, PIC Email `rina.kartika.cb+{runId}-060@qwertysystem.net`, Select Group dikosongkan
11. Pilih node "Area Jakarta" pada tree Select Group
12. Klik `[Submit]`
13. Verifikasi popup tertutup
14. Verifikasi toast sukses "Success, client has been created."
15. Ketik Search `PT Pembuat Satu Kapabilitas {runId}-060`, tekan Enter
16. Verifikasi baris "PT Pembuat Satu Kapabilitas {runId}-060" tampil di sub-tab Active dengan Managed By "Direct"
17. Verifikasi baris "PT Pembuat Satu Kapabilitas {runId}-060": Group "Area Jakarta"

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- TC-584 melanjutkan popup yang sama dengan TC-125 (satu kejadian menutup: submit sukses).
- Temuan untuk QA:
  - Post Condition TC-584 (relasi Partner/Distributor kosong, Default User tanpa App Access dan tanpa Activation Email, Changelog Create) tidak punya langkah observasi; tidak diasersi selain Managed By "Direct".
  - TC-126 (peran sama, bypass FE) ada di spec defense bypass FE.
