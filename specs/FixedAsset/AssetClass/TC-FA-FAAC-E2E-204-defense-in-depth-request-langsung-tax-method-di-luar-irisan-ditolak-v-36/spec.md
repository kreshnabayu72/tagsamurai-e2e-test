---
id: TC-FA-FAAC-E2E-204-defense-in-depth-request-langsung-tax-method-di-luar-irisan-ditolak-v-36
title: "Defense-in-Depth: Request Langsung dengan Tax Method di Luar Irisan Ditolak V-36 pada Create, Edit Versi Scheduled, dan Recommended Classes"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-747
sourceRules: ["V-36", "FAAC-LOGIC-02l", "F-FAAC-01.k7", "F-FAAC-02.k21", "F-FAAC-07.k7", "E-FAAC-68", "E-FAAC-123", "E-FAAC-125", "N-22"]
smoke: []
dependsOn: []
trace:
  "V-36": [4, 7, 10]
  "FAAC-LOGIC-02l": [4, 7, 10]
  "F-FAAC-01.k7": [4, 5]
  "F-FAAC-02.k21": [7, 8]
  "F-FAAC-07.k7": [10, 11]
  "E-FAAC-68": 4
  "E-FAAC-123": 7
  "E-FAAC-125": 10
anchor: [4, 7, 10]
coverage:
  web: automated
---

# Defense-in-Depth: Request Langsung dengan Tax Method di Luar Irisan Ditolak V-36 pada Create, Edit Versi Scheduled, dan Recommended Classes

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite. Spec ini tidak punya langkah UI; semua permintaan memakai sesi akun ini.
- Kemampuan teknis (disediakan tim FE/BE; endpoint dan bentuk request tidak didefinisikan di TC, PRD, atau LLD yang dibaca, sehingga tidak ditulis di spec): klien HTTP atau fixture BE yang mengirim request Create Asset Class, Edit Asset Class, dan Create Recommended Classes dengan sesi aktor ini langsung ke server tanpa melewati browser; kemampuan baca BE untuk jumlah Asset Class dan versi Asset Class `B-IRISAN`; fixture BE untuk menyetel dan membatalkan versi Scheduled Tax Depreciation Class.
- Data Pre-setup bernama literal (seed idempotent): tidak ada Asset Class dengan Class Code `B-V36S`; `Seed Irisan A` (Active; versi Current mengizinkan `Straight Line` dan `Declining Balance`; satu versi Scheduled sejak M+2 hanya mengizinkan `Straight Line`); Asset Class `B-IRISAN` memakai `Seed Irisan A` dengan Tax Method `Straight Line` tanpa versi Scheduled. Versi Scheduled `Bukan bangunan – Kelompok 3` sejak M+2 yang hanya mengizinkan `Straight Line` disetel fixture BE sebagai keadaan awal (TC-744 dan TC-747) di hook `before` dan dibatalkan di hook `after`. Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Jam: M = bulan berjalan menurut zona waktu General Settings client (NC-11); jam server dan jam browser tidak digeser spec ini. Bulan pada Effective From dan tooltip ditulis format `MMM yyyy`; asersi memakai M+n relatif terhadap M. Effective From pada request Edit adalah M+1.
- Data uji request: Class Code `B-V36S`; Tax Depreciation Class `Seed Irisan A`; Tax Method `Declining Balance`; field wajib lain valid dengan nilai dari set Data Uji valid yang disediakan fixture (TC tidak menyebut nilainya; lihat Temuan untuk QA). Baris Recommended Classes `HEAVY-EQ` (Tax Depreciation Class `Bukan bangunan – Kelompok 3`, Tax Method `Declining Balance`).
- State global: versi Scheduled `Bukan bangunan – Kelompok 3` dibatalkan di hook `after`; spec tidak mengubah data lain karena semua permintaan ditolak.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di `suite.md`.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps
1. Catat jumlah Asset Class lewat kemampuan baca BE sebagai baseline N0
2. Atur lewat fixture BE versi Scheduled `Bukan bangunan – Kelompok 3` sejak M+2 yang hanya mengizinkan `Straight Line`
3. Kirim permintaan Create Asset Class langsung ke server dengan Tax Depreciation Class `Seed Irisan A` dan Tax Method `Declining Balance`
4. Verifikasi respons server menolak permintaan dengan caption `Selected tax method is not allowed for this tax depreciation class`
5. Verifikasi jumlah Asset Class sama dengan N0 (Asset Class `B-V36S` tidak dibuat)
6. Kirim permintaan Edit langsung ke server untuk `B-IRISAN` dengan Tax Method `Declining Balance` dan Effective From M+1
7. Verifikasi respons server menolak permintaan dengan caption `Selected tax method is not allowed for this tax depreciation class`
8. Verifikasi `B-IRISAN` tidak memiliki versi baru dan tidak memiliki versi Scheduled lewat kemampuan baca BE
9. Kirim permintaan Create Recommended Classes langsung ke server yang memuat baris `HEAVY-EQ`
10. Verifikasi respons server menolak permintaan dengan caption `Selected tax method is not allowed for this tax depreciation class`
11. Verifikasi jumlah Asset Class sama dengan N0 (tidak ada Asset Class rekomendasi yang dibuat)
12. Batalkan lewat fixture BE versi Scheduled `Bukan bangunan – Kelompok 3` yang disetel pada langkah 2

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-747). Tidak ada TC hanya-BE di spec ini.
- Request langsung (bagian 8b butir 1, K-1): asersi hanya respons server dan state data lewat kemampuan baca BE; tampilan UI tidak diasersi.
- Pembagian TC lintas spec (S-05): TC-747 ada di spec ini (respons server dan state data) dan di spec 206 (klausa "tidak ada entri baru di Changelog Asset Class, System Log, dan Activity Log", log absence kelas g). Spec ini tidak mengasersi log.
- Langkah penghubung (S-03): langkah 1 (baseline N0, S-12), langkah 2 (menyetel keadaan awal TC), dan langkah 12 (memulihkan keadaan awal; fixture BE, hook `after` cadangan).
- Asersi absence langkah 5 dan 11 memakai selisih terhadap baseline N0 dengan anchor positif respons penolakan (langkah 4 dan 10); langkah 8 didahului langkah 7 (bagian 8b butir 2).
- Pengecualian nama literal (S-06, S-12; pengecualian beralasan yang disetujui user): `B-V36S` (tidak pernah tersimpan) dan `B-IRISAN` (hanya dibaca karena permintaan ditolak) adalah seed bertanda `B-*` per TC.
- Temuan untuk QA: TC-747 tidak menyebut status respons dan nilai field wajib lain permintaan Create; spec mengikuti caption V-36 dari TC dan memakai set Data Uji valid fixture.
