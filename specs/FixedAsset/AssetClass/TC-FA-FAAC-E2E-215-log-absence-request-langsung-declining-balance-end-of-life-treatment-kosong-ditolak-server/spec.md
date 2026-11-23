---
id: TC-FA-FAAC-E2E-215-log-absence-request-langsung-declining-balance-end-of-life-treatment-kosong-ditolak-server
title: "Log Absence: Request Langsung Create Declining Balance dengan End-of-Life Treatment Kosong yang Ditolak Server Tidak Menulis Entri di Changelog Asset Class, System Log, dan Activity Log"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-734
sourceRules: ["V-39", "F-FAAC-01.k5", "FAAC-LOGIC-02h"]
smoke: []
dependsOn: []
trace:
  "V-39": [3, 4, 5, 6]
  "F-FAAC-01.k5": [3, 4, 5, 6]
  "FAAC-LOGIC-02h": [3, 4, 5, 6]
coverage:
  web: automated
---

# Log Absence: Request Langsung Create Declining Balance dengan End-of-Life Treatment Kosong yang Ditolak Server Tidak Menulis Entri di Changelog Asset Class, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite. Spec ini tidak punya langkah UI; semua permintaan memakai sesi akun ini.
- Kemampuan teknis (disediakan tim FE/BE; endpoint dan bentuk request tidak didefinisikan di TC, PRD, atau LLD yang dibaca, sehingga tidak ditulis di spec): klien HTTP atau fixture BE yang mengirim request Create Asset Class dengan sesi aktor ini langsung ke server tanpa melewati browser; kemampuan baca BE untuk jumlah entri Changelog Asset Class, System Log akun Total Control (pelaku permintaan), dan Activity Log FAMS (audit trail permanen: asersi memakai selisih terhadap baseline, S-12).
- Pemicu: request langsung kelas a hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji (P-5 butir a). Respons server dan state data Asset Class diasersi di spec 214.
- Data Pre-setup (seed idempotent): tidak ada Asset Class dengan Class Code `B-V39`. Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Data uji request: sama dengan spec 214 (Class Code `B-V39`; Class Name `V39 Test`; Method `Declining Balance`; Useful Life `48`; Declining Rate `50`; End-of-Life Treatment kosong; Depreciation Start Convention `Full month from in-service date`; Tax Depreciation Class `Bukan bangunan – Kelompok 2`; Tax Method `Declining Balance`; Tax Depreciation Start Rule `Month of expenditure`).
- State global: tidak ada yang diubah karena permintaan ditolak.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di `suite.md`.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

1. Catat baseline lewat kemampuan baca BE: jumlah entri Changelog Asset Class, System Log akun Total Control, dan Activity Log FAMS
2. Kirim permintaan Create Asset Class langsung ke server dengan Class Code `B-V39`, Class Name `V39 Test`, Method `Declining Balance`, Useful Life `48`, Declining Rate `50`, End-of-Life Treatment kosong, Depreciation Start Convention `Full month from in-service date`, Tax Depreciation Class `Bukan bangunan – Kelompok 2`, Tax Method `Declining Balance`, dan Tax Depreciation Start Rule `Month of expenditure`
3. Verifikasi respons server menolak permintaan
4. Verifikasi jumlah entri Changelog Asset Class sama dengan baseline
5. Verifikasi jumlah entri System Log akun Total Control sama dengan baseline
6. Verifikasi jumlah entri Activity Log FAMS sama dengan baseline

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-734, bagian "tidak ada entri baru"). Spec absence (kelas g): objek ujinya hanya klausa tidak ada log; request langsung kelas a adalah pemicu (P-5 butir a), sehingga spec ini tidak mengasersi state data Asset Class dan caption validasi.
- Pembagian TC lintas spec (S-05): TC-734 ada di spec 214 (respons server dan state data) dan di spec ini (klausa tidak ada log) dengan permintaan yang sama sebagai aksi nyata dan baseline sendiri.
- Baseline log (S-12): jumlah entri dicatat lewat kemampuan baca BE tepat sebelum pemicu (langkah 1); asersi memakai selisih terhadap baseline, bukan angka absolut.
- Anchor positif asersi absence (bagian 8b butir 2): `Verifikasi` respons server menolak permintaan (langkah 3) mendahului pembacaan jumlah entri sebagai bukti permintaan sudah diproses; pemicu tidak menyentuh entri log yang ada sehingga pembanding berupa jumlah total sebelum dan sesudah (surface agregat).
- Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 (baseline).
- Pengecualian nama literal (S-06, S-12): `B-V39` adalah seed bertanda `B-*` per TC; permintaan ditolak sehingga data tidak berubah.
- Temuan untuk QA: TC-734 menyebut "tidak ada entri baru" tanpa menyebut System Log milik user mana; spec membaca System Log akun pelaku permintaan.
