---
id: TC-FA-FAAC-E2E-206-log-absence-request-langsung-tax-method-di-luar-irisan-ditolak-server
title: "Log Absence: Request Langsung dengan Tax Method di Luar Irisan yang Ditolak Server Tidak Menulis Entri di Changelog Asset Class, System Log, dan Activity Log"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-747
sourceRules: ["V-36", "FAAC-LOGIC-02l", "F-FAAC-01.k7", "F-FAAC-02.k21", "F-FAAC-07.k7"]
smoke: []
dependsOn: []
trace:
  "V-36": [4, 6, 8]
  "F-FAAC-01.k7": [4, 9, 10, 11]
  "F-FAAC-02.k21": 6
  "F-FAAC-07.k7": 8
coverage:
  web: automated
---

# Log Absence: Request Langsung dengan Tax Method di Luar Irisan yang Ditolak Server Tidak Menulis Entri di Changelog Asset Class, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite. Spec ini tidak punya langkah UI; semua permintaan memakai sesi akun ini.
- Kemampuan teknis (disediakan tim FE/BE; endpoint dan bentuk request tidak didefinisikan di TC, PRD, atau LLD yang dibaca, sehingga tidak ditulis di spec): klien HTTP atau fixture BE yang mengirim request Create Asset Class, Edit Asset Class, dan Create Recommended Classes dengan sesi aktor ini langsung ke server tanpa melewati browser; kemampuan baca BE untuk jumlah entri Changelog Asset Class, System Log akun Total Control (pelaku permintaan), dan Activity Log FAMS (audit trail permanen: asersi memakai selisih terhadap baseline, S-12); fixture BE untuk menyetel dan membatalkan versi Scheduled Tax Depreciation Class.
- Pemicu: request langsung kelas a hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji (P-5 butir a). Respons server dan state data diasersi di spec 204.
- Data Pre-setup bernama literal (seed idempotent): tidak ada Asset Class dengan Class Code `B-V36S`; `Seed Irisan A` (Active; versi Current mengizinkan `Straight Line` dan `Declining Balance`; satu versi Scheduled sejak M+2 hanya mengizinkan `Straight Line`); Asset Class `B-IRISAN` memakai `Seed Irisan A` dengan Tax Method `Straight Line` tanpa versi Scheduled. Versi Scheduled `Bukan bangunan – Kelompok 3` sejak M+2 yang hanya mengizinkan `Straight Line` disetel fixture BE sebagai keadaan awal (TC-744 dan TC-747) di hook `before` dan dibatalkan di hook `after`. Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Jam: M = bulan berjalan menurut zona waktu General Settings client (NC-11); jam server dan jam browser tidak digeser spec ini. Bulan pada Effective From dan tooltip ditulis format `MMM yyyy`; asersi memakai M+n relatif terhadap M. Effective From pada request Edit adalah M+1.
- Data uji request: sama dengan spec 204 (Class Code `B-V36S`; Tax Depreciation Class `Seed Irisan A`; Tax Method `Declining Balance`; field wajib lain valid dari set Data Uji valid fixture; baris Recommended Classes `HEAVY-EQ`).
- State global: versi Scheduled `Bukan bangunan – Kelompok 3` dibatalkan di hook `after`; spec tidak mengubah data lain karena semua permintaan ditolak.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di `suite.md`.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps
1. Atur lewat fixture BE versi Scheduled `Bukan bangunan – Kelompok 3` sejak M+2 yang hanya mengizinkan `Straight Line`
2. Catat baseline lewat kemampuan baca BE: jumlah entri Changelog Asset Class, System Log akun Total Control, dan Activity Log FAMS
3. Kirim permintaan Create Asset Class langsung ke server dengan Tax Depreciation Class `Seed Irisan A` dan Tax Method `Declining Balance`
4. Verifikasi respons server menolak permintaan
5. Kirim permintaan Edit langsung ke server untuk `B-IRISAN` dengan Tax Method `Declining Balance` dan Effective From M+1
6. Verifikasi respons server menolak permintaan
7. Kirim permintaan Create Recommended Classes langsung ke server yang memuat baris `HEAVY-EQ`
8. Verifikasi respons server menolak permintaan
9. Verifikasi jumlah entri Changelog Asset Class sama dengan baseline
10. Verifikasi jumlah entri System Log akun Total Control sama dengan baseline
11. Verifikasi jumlah entri Activity Log FAMS sama dengan baseline
12. Batalkan lewat fixture BE versi Scheduled `Bukan bangunan – Kelompok 3` yang disetel pada langkah 1

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-747, bagian "tidak ada entri baru"). Spec absence (kelas g): objek ujinya hanya klausa tidak ada log; request langsung kelas a adalah pemicu (P-5 butir a), sehingga spec ini tidak mengasersi state data Asset Class.
- Pembagian TC lintas spec (S-05): TC-747 ada di spec 204 (respons server dan state data) dan di spec ini (klausa tidak ada log) dengan permintaan yang sama sebagai aksi nyata dan baseline sendiri.
- Baseline log (S-12): jumlah entri dicatat lewat kemampuan baca BE tepat sebelum pemicu (langkah 2); asersi memakai selisih terhadap baseline, bukan angka absolut.
- Anchor positif asersi absence (bagian 8b butir 2): `Verifikasi` respons server menolak ketiga permintaan (langkah 4, 6, 8) mendahului pembacaan jumlah entri sebagai bukti permintaan sudah diproses; pemicu tidak menyentuh entri log yang ada sehingga pembanding berupa jumlah total sebelum dan sesudah (surface agregat).
- Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 (menyetel keadaan awal TC) dan langkah 12 (memulihkannya).
- Pengecualian nama literal (S-06, S-12): `B-V36S` dan `B-IRISAN` adalah seed bertanda `B-*` per TC; semua permintaan ditolak sehingga data tidak berubah.
- Temuan untuk QA: TC-747 menyebut "tidak ada entri baru" tanpa menyebut System Log milik user mana; spec membaca System Log akun pelaku permintaan.
