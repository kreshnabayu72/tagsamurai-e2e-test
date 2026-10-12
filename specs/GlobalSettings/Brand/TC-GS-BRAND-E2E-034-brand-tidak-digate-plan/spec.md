---
id: TC-GS-BRAND-E2E-034-brand-tidak-digate-plan
title: "Brand Tidak Digate Plan: Create Identik di Semua Plan"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-235
coverage:
  web: automated
---

# Brand Tidak Digate Plan: Create Identik di Semua Plan

## Prerequisites

- Mode: FE+BE. Spec membuat dua brand dan mengubah plan Client A (state global).
- Akun: Total Control Client A, `Sari Dewi (Sari D)`, `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > Master Reference > Brand dilakukan sekali di hook `before`.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: mengubah plan Client A lewat API atau alat administrasi (Starter lalu Enterprise) di dalam spec, lalu memuat ulang halaman Brand setelah tiap perubahan plan.
- Hook `before` mencatat plan awal Client A. Hook `after` memulihkan plan Client A ke plan awal dan menghapus `Plan S Co {runId}-034` serta `Plan E Co {runId}-034` lewat API, tanpa berasumsi langkah spec berhasil penuh.
- TC-GS-BRAND-235: Client A berpindah plan Starter lalu Enterprise; data uji `Plan S Co {runId}-034` dan `Plan E Co {runId}-034`.

## Test Steps

### TC-GS-BRAND-235: Brand tidak digate plan: Create identik di semua plan

1. Ubah plan Client A menjadi Starter lewat API atau alat administrasi
2. Muat ulang halaman Global Settings > Master Reference > Brand
3. Klik [+ Brand]
4. Isi Brand Name `Plan S Co {runId}-034`
5. Klik [Submit]
6. Verifikasi toast sukses: "Success, brand has been created."
7. Verifikasi tidak ada dialog upsell dan tidak ada dialog Limit Reached atau limit berbeda dari plan lain pada plan Starter
8. Verifikasi `Plan S Co {runId}-034` tampil di tabel Brand
9. Ubah plan Client A menjadi Enterprise lewat API atau alat administrasi
10. Muat ulang halaman Global Settings > Master Reference > Brand
11. Klik [+ Brand]
12. Isi Brand Name `Plan E Co {runId}-034`
13. Klik [Submit]
14. Verifikasi toast sukses: "Success, brand has been created."
15. Verifikasi tidak ada dialog upsell dan tidak ada dialog Limit Reached atau limit berbeda dari plan lain pada plan Enterprise
16. Verifikasi `Plan E Co {runId}-034` tampil di tabel Brand
17. Verifikasi kedua Create (plan Starter dan Enterprise) sukses tanpa upsell atau limit berbeda
18. Pulihkan plan Client A ke plan awal yang dicatat di hook `before`

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Langkah penghubung (aksi tanpa `Verifikasi`): 1 dan 9 (mengubah plan Client A sesuai precondition TC "Client A berpindah plan Starter lalu Enterprise"), 2 dan 10 (muat ulang halaman Brand sesudah plan berubah) dan 18 (memulihkan plan Client A; hook `after` menjadi cadangan).
- Asersi tambahan: langkah 8 dan 16 (brand tampil di tabel) menjadi bukti konkret makna "sukses" pada Expected Result; Expected Result TC hanya menyebut "keduanya sukses tanpa upsell atau limit berbeda".
- Dua Create dalam satu spec dipakai untuk membandingkan plan Starter dan Enterprise; Client A harus kembali ke plan awal (state global).
- Plan dan lisensi Client A dikelola di luar modul Brand (`foundation/product/licensing/plans.md` §2.1); mekanisme perubahan plan (API atau alat administrasi) disediakan tim FE dan sudah dicatat sebagai kebutuhan di Prerequisites.
- Brand yang dibuat memakai suffix `{runId}-034` (nomor spec).
- Semua TC sumber spec ini dikerjakan di sini; tidak ada TC yang terbelah lintas spec.
