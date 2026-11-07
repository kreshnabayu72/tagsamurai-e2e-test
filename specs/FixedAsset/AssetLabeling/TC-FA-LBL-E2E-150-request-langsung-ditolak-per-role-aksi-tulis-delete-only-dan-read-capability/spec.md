---
id: TC-FA-LBL-E2E-150-request-langsung-ditolak-per-role-aksi-tulis-delete-only-dan-read-capability
title: "Request Langsung Ditolak per Role (Aksi Tulis): Delete-Only dan Read-Capability"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-448
  - TC-FA-LBL-449
  - TC-FA-LBL-450
coverage:
  web: automated
---

# Request Langsung Ditolak per Role (Aksi Tulis): Delete-Only dan Read-Capability

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept. Seluruh langkah berupa request langsung ke server lewat klien HTTP (bagian 8b butir 1): asersi hanya status respons dan state data yang dibaca lewat fixture BE; perilaku FE untuk respons yang sama diasersi di spec jalur form.
- Role yang diuji (sesi API; akun aktor hook `before` adalah Delete-Only, ganti sesi lewat langkah eksplisit; tidak ada login UI):

  | Role | Pre-setup | Akun | Env password |
  |---|---|---|---|
  | Delete-Only | #5 | `Fixture.assetLabeling.akun.deleteOnly` | `Spectra.env.FA_DELETEONLY_PASSWORD` |
  | Read-Capability | #6 | `Fixture.assetLabeling.akun.readCapability` | `Spectra.env.FA_READCAP_PASSWORD` |

- Seeding: label seed dibuat oleh Total Control (Pre-setup #1, `Fixture.assetLabeling.akun.totalControl`, `Spectra.env.FA_LBL_TC_PASSWORD`) lewat fixture BE di hook `before`; hook `after` mengembalikan sesi ke akun default suite.
- Env var: `FA_DELETEONLY_PASSWORD`, `FA_READCAP_PASSWORD`, dan `FA_LBL_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak menulis ulang isinya.
- Data Dinamis (label seed milik spec, bersuffix `{runId}-150`, Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0, bukan Default Label): `Direct Edit 449 {runId}-150`, `Direct Edit 450 {runId}-150`. Label `Direct Create 448` dan `Direct Create 450` serta nama baru `Direct Edit 450 X {runId}-150` tidak di-seed.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |
  | `Fixture.assetLabeling.akun.deleteOnly` | `deleteOnly_automated_{namaCompany}@qwertysystem.net` |
  | `Fixture.assetLabeling.akun.readCapability` | `readCapability_automated_{namaCompany}@qwertysystem.net` |
- Kemampuan teknis (disediakan tim FE/BE, dinyatakan di `suite.md`): klien HTTP untuk request langsung, sesi API (login API password) per role, fixture BE untuk seeding dan membaca state katalog; endpoint tidak ditulis di TC (S-13).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus label seed milik spec lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh.

## Test Steps

### Delete-Only (TC-FA-LBL-448, TC-FA-LBL-449)

1. Gunakan sesi API Delete-Only (Pre-setup #5)
2. Kirim request langsung ke server sebagai Delete-Only: membuat label `Direct Create 448 {runId}-150`
3. Verifikasi server menolak dengan `403 Forbidden`
4. Verifikasi label `Direct Create 448 {runId}-150` tidak ada pada katalog
5. Kirim request langsung ke server sebagai Delete-Only: mengubah nama `Direct Edit 449 {runId}-150` menjadi `Direct Edit 449 X {runId}-150`
6. Verifikasi server menolak dengan `403 Forbidden`
7. Verifikasi label tetap bernama `Direct Edit 449 {runId}-150`

### Read-Capability (TC-FA-LBL-450)

8. Ganti sesi API ke Read-Capability (Pre-setup #6)
9. Kirim request langsung ke server sebagai Read-Capability: membuat label `Direct Create 450 {runId}-150`
10. Verifikasi server menolak pembuatan dengan `403 Forbidden`
11. Kirim request langsung ke server sebagai Read-Capability: mengubah nama label seed `Direct Edit 450 {runId}-150` menjadi `Direct Edit 450 X {runId}-150`
12. Verifikasi server menolak pengubahan dengan `403 Forbidden`
13. Kirim request langsung ke server sebagai Read-Capability: menghapus label seed `Direct Edit 450 {runId}-150`
14. Verifikasi server menolak penghapusan dengan `403 Forbidden`
15. Verifikasi label `Direct Create 450 {runId}-150` tidak ada pada katalog
16. Verifikasi label seed `Direct Edit 450 {runId}-150` masih ada dengan nama yang sama

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 8 (Security & Defense-in-Depth). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03): langkah 1 dan 8 adalah pemilihan atau pergantian sesi API tanpa `Verifikasi`; bukan bagian Expected TC.
- K-1: spec ini memuat TC kelas defense-in-depth (bagian 3 prinsip 13a) dengan Expected respons API; tumpang tindih dengan `tc-settings-asset-labeling-backend.md` dicatat BE pada tingkat endpoint.
- Rujukan S-05 dan prinsip 13g: klausa "tidak ada entri log baru" pada Expected b TC-FA-LBL-448, TC-FA-LBL-449, dan TC-FA-LBL-450 diasersi di spec absence 183 (aksi nyata berupa request yang sama, user dan baseline sendiri per TC); id TC tetap di `sourceTc` spec ini dan spec 183. Spec ini hanya mengasersi status respons dan state data katalog (bagian 8b butir 1).
- Temuan untuk QA:
  - Expected b TC-FA-LBL-448 sampai 450 "tidak ada entri log baru" tidak menyebut surface; spec 183 memakai Changelog Labels, System Log, dan Activity Log.
  - TC-FA-LBL-450 menyebut tiga request dalam satu langkah dengan Expected tunggal; spec memecahnya menjadi tiga request dengan `Verifikasi` `403 Forbidden` masing-masing (S-01).
