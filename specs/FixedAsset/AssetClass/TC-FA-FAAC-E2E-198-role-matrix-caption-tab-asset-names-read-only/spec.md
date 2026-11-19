---
id: TC-FA-FAAC-E2E-198-role-matrix-caption-tab-asset-names-read-only
title: "Role Matrix: Caption Tab Asset Names Tidak Tampil bagi Read Only"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-738
sourceRules: ["ST-37", "§4.1.3#p1", "§4.8#r21"]
smoke: []
dependsOn: []
trace:
  "ST-37": 6
  "§4.1.3#p1": [4, 6]
  "§4.8#r21": 5
coverage:
  web: automated
---

# Role Matrix: Caption Tab Asset Names Tidak Tampil bagi Read Only

## Prerequisites

- Mode: FE+BE.
- Login akun Read Only dilakukan di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Role yang diuji:

| Role | Akun | Env var password | TC |
|---|---|---|---|
| Read Only | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_RO_PASSWORD` | TC-FA-FAAC-738 |

- Env var: `FA_AC_RO_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`).
- Rujukan suite: seed data lewat API/fixture BE dan flag Guided Tooltip mengikuti `suite.md` (butir Hook suite). Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Asset Class HEAVY-EQ (Example Data PRD §4.1.1) dengan Asset Name ter-assign Excavator PC200 dan Wheel Loader. Dibaca, tidak diubah. Identitasnya dirujuk lewat `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada; nama kunci ditetapkan tim FE).
- Tabel Asset Class memuat baris lain di luar sembilan Asset Class contoh; baris HEAVY-EQ dicari lewat Search karena tidak dijamin berada di halaman 1.
- Data Dinamis: tidak ada. State global yang diubah: tidak ada selain sesi akun (dipulihkan hook `after`).

## Test Steps

### TC-FA-FAAC-738: Caption tab Asset Names tidak tampil bagi Read Only

1. Ketik Search `HEAVY-EQ`, tekan Enter
2. Klik link Class Code "HEAVY-EQ"
3. Klik tab "Asset Names"
4. Verifikasi tabel Asset Names tampil dengan baris Wheel Loader
5. Verifikasi tombol "+ Assign Asset Names" Hidden
6. Verifikasi caption "Changes on this tab are applied immediately." tidak tampil di bawah judul SectionCard tabel

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`. Spec Role Matrix (bagian 3a konvensi) untuk satu role; role lain dengan hak Update dicakup spec 197 (caption tampil).
- Langkah penghubung (S-03): langkah 1 (Search baris HEAVY-EQ, 8b.13), langkah 2 dan 3 (navigasi).
- Langkah 5 dan 6 adalah asersi absence; anchor positifnya langkah 4 (tabel tab Asset Names tampil dengan baris Wheel Loader) (8b.2).
- Temuan untuk QA: TC-738 tidak menyebut baris yang dipakai sebagai anchor tab Asset Names; spec memakai Wheel Loader, Asset Name seed HEAVY-EQ yang juga dipakai spec 022.
