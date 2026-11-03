---
id: TC-FA-CAID-E2E-028-defense-in-depth-initial-company-request-langsung
title: "Defense-in-Depth: Request Save Langsung dengan Initial Company Berkarakter Terlarang dan Lebih dari 5 Karakter"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAID-337
  - TC-FA-CAID-338
coverage:
  web: automated
---

# Defense-in-Depth: Request Save Langsung dengan Initial Company Berkarakter Terlarang dan Lebih dari 5 Karakter

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control Company Alpha (Pre-setup No 1, `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`); halaman Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip disetel seen untuk akun UI suite; konfigurasi Company Alpha dipulihkan ke baseline B1 dan aset A1 sampai A5 (Pre-setup No 11) ke kondisi awal di `beforeEach` dan `after` lewat sesi API aktor (klien HTTP dan token sesi API disediakan tim FE; token tidak dihitung sebagai sesi web).
- Data Pre-setup No 10: baseline B1 (Master Switch ON, Separator `/ (Slash)`, segmen tercentang Group Code, Category Code, Asset Name Code, Purchase Date, Asset Increment, tanpa Initial Company). Nilai dibaca dari `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE): penyunting request pada sesi otomasi (Pre-setup No 26) untuk mengubah payload request Save yang dikirim dari browser (langkah 2 dan 9); konfirmasi otomatis dialog `beforeunload` bawaan browser oleh harness untuk muat ulang pada form yang belum disimpan (langkah 5 dan 12).
- State: tidak ada perubahan tersimpan yang diharapkan. Hook `after` suite memulihkan baseline.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-337: Initial Company berisi karakter di luar A-Z dan 0-9 tidak mengubah konfigurasi

1. Pilih Separator `- (Dash)`
2. Ubah payload request Save lewat penyunting sehingga entry Initial Company dicentang dengan nilai `AB-1!`
3. Klik `[Save]`
4. Tunggu aksi selesai
5. Muat ulang tab Custom Asset ID
6. Verifikasi konfigurasi tersimpan tidak berubah: Separator tetap `/ (Slash)`
7. Verifikasi checkbox `Initial Company` tidak tercentang

### TC-FA-CAID-338: Initial Company lebih dari 5 karakter tidak mengubah konfigurasi

8. Pilih Separator `- (Dash)`
9. Ubah payload request Save lewat penyunting sehingga entry Initial Company dicentang dengan nilai `ABCDEF`
10. Klik `[Save]`
11. Tunggu aksi selesai
12. Muat ulang tab Custom Asset ID
13. Verifikasi konfigurasi tersimpan tidak berubah: Separator tetap `/ (Slash)`
14. Verifikasi checkbox `Initial Company` tidak tercentang

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- `K-1`: spec defense-in-depth dengan Expected state data tetap FE+BE walau tumpang tindih dengan `tc-settings-custom-asset-id-backend.md`; TC granular tetap sumber dan BE mencatatnya pada tingkat endpoint.
- Sesuai G-13 di catatan TC, perilaku server atas Initial Company terlarang atau lebih dari 5 karakter pada request langsung tidak dinyatakan PRD; spec hanya mengasersi konfigurasi tersimpan tidak berubah dan tidak mengasersi respons maupun pesan UI.
- Langkah penghubung (tanpa `Verifikasi`): langkah 4 dan 11 (Tunggu aksi selesai sebelum muat ulang, karena hasil `[Save]` tidak diasersi); muat ulang pada langkah 5 dan 12 terjadi pada form yang masih dirty dan dikonfirmasi harness sesuai Prerequisites, sehingga form berakhir pristine pada nilai tersimpan.
- Temuan untuk QA:
  - Expected TC-FA-CAID-337 b dan TC-FA-CAID-338 b ("tidak ada entri log baru" pada Changelog, System Log, dan Activity Log) tidak diasersi di spec kelas a ini (S-05); asersi itu ada di spec absence 099 yang memuat TC-FA-CAID-337 dan 338 dengan request ini sebagai pemicu dan baseline sendiri. Langkah Uji TC-FA-CAID-337 dan 338 yang membuka Modal Changelog, System Log, dan Activity Log hanya melayani asersi absence tersebut.
