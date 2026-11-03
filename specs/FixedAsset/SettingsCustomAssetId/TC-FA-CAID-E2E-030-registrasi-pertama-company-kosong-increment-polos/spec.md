---
id: TC-FA-CAID-E2E-030-registrasi-pertama-company-kosong-increment-polos
title: "Registrasi Aset pada Company Kosong Tanpa Konfigurasi Memakai Increment Polos"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-262
coverage:
  web: automated
---

# Registrasi Aset pada Company Kosong Tanpa Konfigurasi Memakai Increment Polos

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control Company Kosong (Pre-setup No 12). Email akun disediakan tim FE/BE (Pre-setup No 12 TC). Password dari `Spectra.env.FA_KOSONG_TC_PASSWORD` (kolom Akun dan Env Var Pre-setup No 12). Halaman Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka hook `beforeEach` suite; langkah 1 membuka layar awal TC yang berbeda.
- Data Pre-setup No 12: Company Kosong tanpa konfigurasi tersimpan dan tanpa aset. Master data untuk registrasi: Asset Name `ThinkPad T490`, Brand `Lenovo`, Model/Type `T490`, Group `Jakarta Office`, Condition `Normal` (Pre-setup TC No 24 untuk Company Register; ketersediaan pada Company Kosong disediakan tim FE). Nilai dibaca dari `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Data Dinamis No 5: dua aset Draft hasil Quick Register pada Company Kosong (Increment polos 1 dan 2), dibuat oleh langkah 2 dan 3 melalui UI.
- Kemampuan teknis (disediakan tim FE/BE): reset Company Kosong ke kondisi tanpa konfigurasi tersimpan dan tanpa aset lewat sesi API aktor (klien HTTP dan token sesi API; token tidak dihitung sebagai sesi web), dijalankan di hook `before` dan `after` spec ini.
- State: spec ini membuat dua aset pada Company Kosong. Pemulihan: hook `after` mereset Company Kosong dan mengembalikan sesi ke akun default suite (Total Control Company Alpha, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-262: Konfigurasi belum pernah disimpan: registrasi memakai Increment polos

1. Buka Fixed Asset > Assets > Registration
2. Klik `[+ Quick Register]`, pilih Asset Name `ThinkPad T490`, Brand `Lenovo`, Model/Type `T490`, Group `Jakarta Office`, Condition `Normal`, lalu klik `[Save as Draft]`
3. Ulangi registrasi kedua dengan data yang sama
4. Tunggu aksi selesai: tombol `[Save as Draft]` selesai diproses
5. Buka Fixed Asset > Assets > All Assets
6. Verifikasi Asset ID aset pertama `1` sebagai bilangan bulat polos tanpa padding nol, tanpa pemisah, dan tanpa segmen lain
7. Verifikasi Asset ID aset kedua `2` sebagai bilangan bulat polos tanpa padding nol, tanpa pemisah, dan tanpa segmen lain
8. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID
9. Verifikasi form menampilkan Master Switch ON

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa `Verifikasi`): langkah 5 dan 8 (membuka layar tempat Asset ID dan form diamati). Langkah 3 mengulang langkah 2 sesuai Langkah Uji TC. Langkah 4 adalah "Tunggu aksi selesai" (bagian 8b butir 8): `[Save as Draft]` pada langkah 2 dan 3 tidak punya asersi hasil langsung dan langkah 5 berpindah surface.
- Pembagian TC lintas spec: TC-FA-CAID-44 sampai TC-FA-CAID-47 (Create konfigurasi pertama pada Company Kosong) ada di spec 015.
- Temuan untuk QA:
  - Data master `ThinkPad T490`, Brand `Lenovo`, dan Group `Jakarta Office` pada Company Kosong tidak didefinisikan di Pre-setup TC (Pre-setup No 12 hanya menyebut tanpa konfigurasi dan tanpa aset).
