---
id: TC-FA-FAAC-E2E-214-defense-in-depth-request-langsung-declining-balance-end-of-life-treatment-kosong-ditolak-v-39
title: "Defense-in-Depth: Request Langsung Create Declining Balance dengan End-of-Life Treatment Kosong Ditolak V-39"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-734
sourceRules: ["V-39", "F-FAAC-01.k5", "E-FAAC-05", "FAAC-LOGIC-02h"]
smoke: []
dependsOn: []
trace:
  "V-39": [3, 4]
  "F-FAAC-01.k5": [3, 4]
  "E-FAAC-05": 3
  "FAAC-LOGIC-02h": [3, 4]
anchor: [3]
coverage:
  web: automated
---

# Defense-in-Depth: Request Langsung Create Declining Balance dengan End-of-Life Treatment Kosong Ditolak V-39

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite. Spec ini tidak punya langkah UI; semua permintaan memakai sesi akun ini.
- Kemampuan teknis (disediakan tim FE/BE; endpoint dan bentuk request tidak didefinisikan di TC, PRD, atau LLD yang dibaca, sehingga tidak ditulis di spec): klien HTTP atau fixture BE yang mengirim request Create Asset Class dengan sesi aktor ini langsung ke server tanpa melewati browser; kemampuan baca BE untuk jumlah Asset Class dan keberadaan Asset Class berdasarkan Class Code.
- Data Pre-setup (seed idempotent): tidak ada Asset Class dengan Class Code `B-V39`. Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Data uji request (dari TC-734): Class Code `B-V39`; Class Name `V39 Test`; Method `Declining Balance`; Useful Life `48`; Declining Rate `50`; End-of-Life Treatment kosong; Depreciation Start Convention `Full month from in-service date`; Tax Depreciation Class `Bukan bangunan – Kelompok 2`; Tax Method `Declining Balance`; Tax Depreciation Start Rule `Month of expenditure`.
- State global: tidak ada yang diubah karena permintaan ditolak; tidak ada cleanup selain pemulihan seed bila fixture BE menyiapkannya.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di `suite.md`.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

1. Catat jumlah Asset Class lewat kemampuan baca BE sebagai baseline N0
2. Kirim permintaan Create Asset Class langsung ke server dengan Class Code `B-V39`, Class Name `V39 Test`, Method `Declining Balance`, Useful Life `48`, Declining Rate `50`, End-of-Life Treatment kosong, Depreciation Start Convention `Full month from in-service date`, Tax Depreciation Class `Bukan bangunan – Kelompok 2`, Tax Method `Declining Balance`, dan Tax Depreciation Start Rule `Month of expenditure`
3. Verifikasi respons server menolak permintaan dengan caption validasi `End-of-life treatment must not be empty`
4. Verifikasi Asset Class `B-V39` tidak dibuat (jumlah Asset Class sama dengan N0)

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-734). Tidak ada TC hanya-BE di spec ini: TC-734 berkelas defense-in-depth dengan Expected respons API dan state data, sehingga masuk spec FE+BE (K-1, konvensi bagian 2).
- Request langsung (bagian 8b butir 1, K-1): asersi hanya respons server dan state data lewat kemampuan baca BE; tampilan UI tidak diasersi.
- Pembagian TC lintas spec (S-05): TC-734 ada di spec ini (respons server dan state data) dan di spec 215 (klausa "tidak ada entri baru di Changelog Asset Class, System Log, maupun Activity Log", log absence kelas g). Spec ini tidak mengasersi log.
- Langkah penghubung (S-03): langkah 1 (baseline N0, S-12). Asersi absence langkah 4 memakai selisih terhadap baseline N0 dengan anchor positif respons penolakan pada langkah 3 (bagian 8b butir 2).
- Pengecualian nama literal (S-06, S-12; pengecualian beralasan yang disetujui user): `B-V39` adalah seed bertanda `B-*` per TC (tidak pernah tersimpan karena permintaan ditolak).
- Temuan untuk QA: TC-734 tidak menyebut status respons HTTP; spec hanya mengasersi penolakan dan caption `End-of-life treatment must not be empty`. Kolom FE TC-734 bertanda `-` dan kolom BE bertanda `v` (pola yang sama dengan TC-747); spec ini tetap dibuat karena TC granular tetap sumber dan K-1 (konvensi bagian 2) mengharuskan TC defense-in-depth berasersi respons API masuk spec FE+BE, sehingga TC-734 tidak dicatat sebagai hanya-BE.
