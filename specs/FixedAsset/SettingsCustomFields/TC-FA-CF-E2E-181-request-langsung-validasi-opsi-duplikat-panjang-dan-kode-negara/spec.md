---
id: TC-FA-CF-E2E-181-request-langsung-validasi-opsi-duplikat-panjang-dan-kode-negara
title: "Request Langsung Ditolak: Opsi Duplikat, Panjang Field Name, dan Kode Negara"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-573
  - TC-FA-CF-574
  - TC-FA-CF-593
coverage:
  web: automated
---

# Request Langsung Ditolak: Opsi Duplikat, Panjang Field Name, dan Kode Negara

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Alpha (Pre-setup #11 dan #12). Nilai data mengacu `Fixture.faCustomFields.baselineGeneral` (fixture disediakan tim FE).
- Data Dinamis: Field Name request ditolak `Req 573 {runId}-181`, `Req 574 {runId}-181` (diperpanjang dengan karakter `X` sampai tepat 121 karakter termasuk suffix), dan `Contact number {runId}-181`; tidak ada yang tersimpan. Cleanup di hook `after`: hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-181`.
- Kemampuan teknis: klien HTTP dengan token Total Control Company Alpha (sesi API aktor, lihat `suite.md`; kemampuan disediakan tim BE/FE); fixture BE untuk membaca field tersimpan.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-573: nama opsi duplikat

1. Kirim request Create Dropdown langsung dengan opsi `Gold` dan `gold` dan Field Name `Req 573 {runId}-181`
2. Verifikasi server menolak request
3. Verifikasi pesan `Option name already exists` terkait opsi

### TC-FA-CF-574: Field Name lebih dari 120 karakter

4. Kirim request Create langsung dengan Field Name 121 karakter (`Req 574 {runId}-181` diikuti karakter `X`)
5. Verifikasi server menolak request
6. Verifikasi pesan `Max. 120 characters`
7. Verifikasi tidak ada mutasi (field tidak tersimpan, dibaca lewat fixture BE)

### TC-FA-CF-593: Global Value Phone dengan kode negara tidak ada di katalog

8. Kirim request Create Phone Global langsung dengan Field Name `Contact number {runId}-181` dan kode negara `+999`
9. Verifikasi server menolak dengan 422
10. Verifikasi pesan inline `Contact number {runId}-181 must include a valid country code`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- K-1: TC kelas a dengan Expected respons API (TC-FA-CF-573, 574, 593) tetap di spec FE+BE ini; request hanya mengasersi status respons, pesan, dan state data lewat fixture BE (bagian 8b butir 1). TC request langsung validasi lainnya ada di spec 151.
- S-05: TC-FA-CF-572 (Scope berisi Asset Name yang sudah tidak ada, dengan klausa "tanpa entri log dari request ini") diasersi di spec 132 beserta baseline log; spec ini tidak memuat asersi log.
- Temuan untuk QA:
  - TC-FA-CF-573 dan 574 tidak menyebut kode status penolakan; TC-FA-CF-573 hanya menyebut pesan "terkait opsi".
  - TC-FA-CF-593 menyebut pesan `Contact number must include a valid country code`; spec memakai Field Name bersuffix sehingga pesan memuat nama itu (pola `[Field name] must include a valid country code`).
