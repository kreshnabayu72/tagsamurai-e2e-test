---
id: TC-GS-BRAND-E2E-010-role-matrix-negatif-tanpa-capability
title: "Role Matrix Negatif: Aktor Tanpa Capability Tidak Dapat Mengakses Tab Brand"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-BRAND-33
  - TC-GS-BRAND-34
coverage:
  web: automated
---

# Role Matrix Negatif: Aktor Tanpa Capability Tidak Dapat Mengakses Tab Brand

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-GS-BRAND-33, TC-GS-BRAND-34 | Tanpa Capability (bukan Total Control dan bukan Read Only) | Fajar Nugroho | `noCapability_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_NOCAP_PASSWORD` |

- Login akun Tanpa Capability dilakukan di hook `before` spec ini (kredensial dari env var di atas); hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture; nama env `GS_NOCAP_PASSWORD` didaftarkan di `executionConfig.environmentVariables`.
- Data Pre-setup Client A (12 brand, data environment tetap) tersedia sehingga ketiadaan baris Brand di layar memang disebabkan oleh izin, bukan data kosong. Spec tidak membuat atau menghapus data.
- Fixture `fixtures/brand.json` (belum ada, disiapkan tim FE):

| Kunci | Isi | Dipakai di |
|---|---|---|
| `urlTabBrand` | URL langsung Tab Brand (Global Settings > Master Reference > Brand) | TC-GS-BRAND-34 (Data Uji) |

- Guided Tooltip: tidak relevan karena aktor tidak dapat membuka Tab Brand. Tidak ada state global yang diubah.

## Test Steps

### TC-GS-BRAND-33: Aktor tanpa capability dan bukan Total Control/Read Only tidak melihat Tab Brand

1. Buka Global Settings
2. Cari Master Reference / Tab Brand
3. Verifikasi Tab `Brand` Hidden
4. Verifikasi data Brand tidak dapat dilihat

### TC-GS-BRAND-34: Akses langsung URL Tab Brand tanpa capability ditolak

5. Ketik langsung URL Tab Brand (`urlTabBrand`) di address bar browser
6. Verifikasi toast error: "You don't have permission to do this."
7. Verifikasi UI di-refresh
8. Verifikasi tidak ada redirect ke halaman lain
9. Verifikasi tidak ada baris Brand termuat

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix negatif (bagian 3a konvensi) untuk satu role. Role negatif lain tidak ditulis di sini karena tidak ada TC sumbernya; visibilitas elemen per role lain diuji di spec `TC-GS-BRAND-E2E-009-role-matrix-visibilitas-elemen-per-role`.
- Tidak ada langkah penghubung; fixture `urlTabBrand` sudah dicatat sebagai kebutuhan di Prerequisites.
