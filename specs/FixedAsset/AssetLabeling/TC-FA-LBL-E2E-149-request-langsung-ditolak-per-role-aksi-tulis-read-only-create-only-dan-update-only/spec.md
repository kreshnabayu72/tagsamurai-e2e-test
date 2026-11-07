---
id: TC-FA-LBL-E2E-149-request-langsung-ditolak-per-role-aksi-tulis-read-only-create-only-dan-update-only
title: "Request Langsung Ditolak per Role (Aksi Tulis): Read Only, Create-Only, dan Update-Only"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-441
  - TC-FA-LBL-442
  - TC-FA-LBL-443
  - TC-FA-LBL-444
  - TC-FA-LBL-445
  - TC-FA-LBL-446
  - TC-FA-LBL-447
coverage:
  web: automated
---

# Request Langsung Ditolak per Role (Aksi Tulis): Read Only, Create-Only, dan Update-Only

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept. Seluruh langkah berupa request langsung ke server lewat klien HTTP (bagian 8b butir 1): asersi hanya status respons dan state data yang dibaca lewat fixture BE; perilaku FE untuk respons yang sama diasersi di spec jalur form.
- Role yang diuji (sesi API; akun aktor hook `before` adalah Read Only, ganti sesi lewat langkah eksplisit; tidak ada login UI):

  | Role | Pre-setup | Akun | Env password |
  |---|---|---|---|
  | Read Only | #2 | `Fixture.assetLabeling.akun.readOnly` | `Spectra.env.FA_RO_PASSWORD` |
  | Create-Only | #3 | `Fixture.assetLabeling.akun.createOnly` | `Spectra.env.FA_CREATEONLY_PASSWORD` |
  | Update-Only | #4 | `Fixture.assetLabeling.akun.updateOnly` | `Spectra.env.FA_UPDATEONLY_PASSWORD` |

- Seeding: label seed dibuat oleh Total Control (Pre-setup #1, `Fixture.assetLabeling.akun.totalControl`, `Spectra.env.FA_LBL_TC_PASSWORD`) lewat fixture BE di hook `before`; hook `after` mengembalikan sesi ke akun default suite.
- Env var: `FA_RO_PASSWORD`, `FA_CREATEONLY_PASSWORD`, `FA_UPDATEONLY_PASSWORD`, dan `FA_LBL_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak menulis ulang isinya.
- Data Dinamis (label seed milik spec, bersuffix `{runId}-149`, Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0, bukan Default Label): `Direct Edit 442 {runId}-149`, `Direct Delete 443 {runId}-149`, `Direct Edit 444 {runId}-149`, `Direct Delete 445 {runId}-149`, `Direct Delete 447 {runId}-149`. Label `Direct Create 441`, `Direct Create 446` tidak di-seed (hasil request yang ditolak tidak boleh ada).
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |
  | `Fixture.assetLabeling.akun.readOnly` | `readOnly_automated_{namaCompany}@qwertysystem.net` |
  | `Fixture.assetLabeling.akun.createOnly` | `createOnly_automated_{namaCompany}@qwertysystem.net` |
  | `Fixture.assetLabeling.akun.updateOnly` | `updateOnly_automated_{namaCompany}@qwertysystem.net` |
- Kemampuan teknis (disediakan tim FE/BE, dinyatakan di `suite.md`): klien HTTP untuk request langsung, sesi API (login API password) per role, fixture BE untuk seeding dan membaca state katalog; endpoint tidak ditulis di TC (S-13).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus label seed milik spec lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh.

## Test Steps

### Read Only (TC-FA-LBL-441, TC-FA-LBL-442, TC-FA-LBL-443)

1. Gunakan sesi API Read Only (Pre-setup #2)
2. Kirim request langsung ke server sebagai Read Only: membuat label `Direct Create 441 {runId}-149`
3. Verifikasi server menolak dengan `403 Forbidden`
4. Verifikasi label `Direct Create 441 {runId}-149` tidak ada pada katalog
5. Kirim request langsung ke server sebagai Read Only: mengubah nama `Direct Edit 442 {runId}-149` menjadi `Direct Edit 442 X {runId}-149`
6. Verifikasi server menolak dengan `403 Forbidden`
7. Verifikasi label tetap bernama `Direct Edit 442 {runId}-149`
8. Kirim request langsung ke server sebagai Read Only: menghapus label bersih `Direct Delete 443 {runId}-149`
9. Verifikasi server menolak dengan `403 Forbidden`
10. Verifikasi label `Direct Delete 443 {runId}-149` masih ada pada katalog

### Create-Only (TC-FA-LBL-444, TC-FA-LBL-445)

11. Ganti sesi API ke Create-Only (Pre-setup #3)
12. Kirim request langsung ke server sebagai Create-Only: mengubah nama `Direct Edit 444 {runId}-149` menjadi `Direct Edit 444 X {runId}-149`
13. Verifikasi server menolak dengan `403 Forbidden`
14. Verifikasi label tetap bernama `Direct Edit 444 {runId}-149`
15. Kirim request langsung ke server sebagai Create-Only: menghapus label bersih `Direct Delete 445 {runId}-149`
16. Verifikasi server menolak dengan `403 Forbidden`
17. Verifikasi label `Direct Delete 445 {runId}-149` masih ada pada katalog

### Update-Only (TC-FA-LBL-446, TC-FA-LBL-447)

18. Ganti sesi API ke Update-Only (Pre-setup #4)
19. Kirim request langsung ke server sebagai Update-Only: membuat label `Direct Create 446 {runId}-149`
20. Verifikasi server menolak dengan `403 Forbidden`
21. Verifikasi label `Direct Create 446 {runId}-149` tidak ada pada katalog
22. Kirim request langsung ke server sebagai Update-Only: menghapus label bersih `Direct Delete 447 {runId}-149`
23. Verifikasi server menolak dengan `403 Forbidden`
24. Verifikasi label `Direct Delete 447 {runId}-149` masih ada pada katalog

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 8 (Security & Defense-in-Depth). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03): langkah 1, 11, 18 adalah pemilihan atau pergantian sesi API tanpa `Verifikasi`; bukan bagian Expected TC.
- K-1: spec ini memuat TC kelas defense-in-depth (bagian 3 prinsip 13a) dengan Expected respons API; tumpang tindih dengan `tc-settings-asset-labeling-backend.md` dicatat BE pada tingkat endpoint.
- Rujukan S-05 dan prinsip 13g: klausa "tidak ada entri log baru" pada Expected b TC-FA-LBL-441, TC-FA-LBL-442, TC-FA-LBL-443, TC-FA-LBL-444, TC-FA-LBL-445, TC-FA-LBL-446, dan TC-FA-LBL-447 diasersi di spec absence 183 (aksi nyata berupa request yang sama, user dan baseline sendiri per TC); id TC tetap di `sourceTc` spec ini dan spec 183. Spec ini hanya mengasersi status respons dan state data katalog (bagian 8b butir 1).
- Penentuan akun dan sesi: seluruh langkah memakai sesi API, jadi ganti sesi antar-role (langkah penghubung) tidak memerlukan login UI (S-07).
- Temuan untuk QA:
  - Expected b TC-FA-LBL-441 sampai 447 "tidak ada entri log baru" tidak menyebut surface; spec 183 memakai Changelog Labels, System Log, dan Activity Log.
  - Nama baru pada TC-FA-LBL-442, 444, dan 449 ditulis `Direct Edit nnn X`; spec memakai nama bersuffix `{runId}` dan akhiran ` X` setelah suffix supaya unik per run.
