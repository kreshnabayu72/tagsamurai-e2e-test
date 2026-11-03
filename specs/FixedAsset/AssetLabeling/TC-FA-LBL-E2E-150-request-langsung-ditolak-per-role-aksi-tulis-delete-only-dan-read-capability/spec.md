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
- Env var: `FA_DELETEONLY_PASSWORD`, `FA_READCAP_PASSWORD`, dan `FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak menulis ulang isinya.
- Data Dinamis (label seed milik spec, bersuffix `{runId}-150`, Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0, bukan Default Label): `Direct Edit 449 {runId}-150`, `Direct Edit 450 {runId}-150`. Label `Direct Create 448` dan `Direct Create 450` serta nama baru `Direct Edit 450 X {runId}-150` tidak di-seed.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |
  | `Fixture.assetLabeling.akun.deleteOnly` | `deleteOnly_automated_{namaCompany}@qwertysystem.net` |
  | `Fixture.assetLabeling.akun.readCapability` | `readCapability_automated_{namaCompany}@qwertysystem.net` |
- Kemampuan teknis (disediakan tim FE/BE, dinyatakan di `suite.md`): klien HTTP untuk request langsung, sesi API (login API password) per role, fixture BE untuk seeding dan membaca state katalog serta jumlah entri Changelog Labels, System Log, dan Activity Log; endpoint tidak ditulis di TC (S-13).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus label seed milik spec lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh.

## Test Steps

### Persiapan baseline

1. Catat baseline jumlah entri Changelog Labels, System Log, dan Activity Log lewat fixture BE

### Delete-Only (TC-FA-LBL-448, TC-FA-LBL-449)

2. Gunakan sesi API Delete-Only (Pre-setup #5)
3. Kirim request langsung ke server sebagai Delete-Only: membuat label `Direct Create 448 {runId}-150`
4. Verifikasi server menolak dengan `403 Forbidden`
5. Verifikasi label `Direct Create 448 {runId}-150` tidak ada pada katalog
6. Verifikasi jumlah entri Changelog Labels, System Log, dan Activity Log sama dengan baseline
7. Kirim request langsung ke server sebagai Delete-Only: mengubah nama `Direct Edit 449 {runId}-150` menjadi `Direct Edit 449 X {runId}-150`
8. Verifikasi server menolak dengan `403 Forbidden`
9. Verifikasi label tetap bernama `Direct Edit 449 {runId}-150`
10. Verifikasi jumlah entri Changelog Labels, System Log, dan Activity Log sama dengan baseline

### Read-Capability (TC-FA-LBL-450)

11. Ganti sesi API ke Read-Capability (Pre-setup #6)
12. Kirim request langsung ke server sebagai Read-Capability: membuat label `Direct Create 450 {runId}-150`
13. Verifikasi server menolak pembuatan dengan `403 Forbidden`
14. Kirim request langsung ke server sebagai Read-Capability: mengubah nama label seed `Direct Edit 450 {runId}-150` menjadi `Direct Edit 450 X {runId}-150`
15. Verifikasi server menolak pengubahan dengan `403 Forbidden`
16. Kirim request langsung ke server sebagai Read-Capability: menghapus label seed `Direct Edit 450 {runId}-150`
17. Verifikasi server menolak penghapusan dengan `403 Forbidden`
18. Verifikasi label `Direct Create 450 {runId}-150` tidak ada pada katalog
19. Verifikasi label seed `Direct Edit 450 {runId}-150` masih ada dengan nama yang sama
20. Verifikasi jumlah entri Changelog Labels, System Log, dan Activity Log sama dengan baseline

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 8 (Security & Defense-in-Depth). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03): langkah 1, 2, 11 adalah navigasi, pembukaan atau penutupan modal, drawer, dialog, atau pengaturan state seeding tanpa `Verifikasi`; bukan bagian Expected TC.
- K-1: spec ini memuat TC kelas defense-in-depth (bagian 3 prinsip 13a) dengan Expected respons API; tumpang tindih dengan `tc-settings-asset-labeling-backend.md` dicatat BE pada tingkat endpoint.
- Asersi "tidak ada entri log baru" ditulis sebagai asersi jumlah entri Changelog Labels, System Log, dan Activity Log terhadap baseline (bagian 3 prinsip 13g: asersi jumlah bukan kelas g; S-12). Suite ini tidak memuat spec absence untuk TC ini, sehingga tidak ada rujukan ke spec lain (S-05).
- Temuan untuk QA:
  - Expected b TC-FA-LBL-448 sampai 450 "tidak ada entri log baru" tidak menyebut surface; spec memakai Changelog Labels, System Log, dan Activity Log (asersi jumlah dengan baseline); lihat catatan keputusan pada spec 149.
  - TC-FA-LBL-450 menyebut tiga request dalam satu langkah dengan Expected tunggal; spec memecahnya menjadi tiga request dengan `Verifikasi` `403 Forbidden` masing-masing (S-01).
