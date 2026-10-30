---
id: TC-GS-UCF-E2E-076-multi-tab-create-bersamaan
title: "Multi-Tab: Submit Ganda Create Field Name Sama melalui Dua Tab pada Satu Sesi Tidak Menduplikasi Definisi"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-UCF-324
coverage:
  web: automated
---

# Multi-Tab: Submit Ganda Create Field Name Sama melalui Dua Tab pada Satu Sesi Tidak Menduplikasi Definisi

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`).
- Akun aktor (login di hook `before`; password hanya lewat env var, tidak ditulis di spec atau fixture): Total Control Client A (Sari Dewi, Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1), `Spectra.env.GS_TC_PASSWORD`. Kedua tab memakai sesi login yang sama.
- Dua tab browser pada satu sesi (kelas multi-konteks, multi-tab): Tab 1 adalah tab hook `beforeEach` yang sudah membuka Global Settings > User > Custom Field; Tab 2 dibuka oleh langkah spec ini.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-custom-field-user` true untuk akun aktor dan hook `after` memulihkannya, lihat `suite.md`.
- Data Pre-setup tidak dipakai.
- Data Dinamis milik spec (nama bersuffix `{runId}-076`; fixture baru `Fixture.customFieldUser.multiTab076`, belum ada; tidak di-seed, dibuat oleh aksi uji; Text, Required No): `Idem Probe {runId}-076`.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): hapus lewat API semua Custom Field bersuffix `{runId}-076` pada Client A; tutup Tab 2.
- Kemampuan teknis: dua tab pada satu sesi browser; langkah dijalankan berurutan dengan penanda `[Tab 1]` dan `[Tab 2]`.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite).

## Test Steps

### TC-GS-UCF-324: Submit ganda melalui dua tab tidak menduplikasi definisi

1. [Tab 1] Klik `[+ Custom Field]`, isi Field Name `Idem Probe {runId}-076`, Data Type `Text`
2. [Tab 2] Buka Global Settings > User > Custom Field, klik `[+ Custom Field]`, isi Field Name `Idem Probe {runId}-076`, Data Type `Text`
3. [Tab 1] Klik `[Submit]`
4. [Tab 2] Klik `[Submit]`
5. [Tab 2] Verifikasi error inline `Field name already exists`
6. [Tab 1] Ketik Search `Idem Probe {runId}-076`, tekan Enter
7. [Tab 1] Verifikasi tabel hanya memuat satu baris `Idem Probe {runId}-076`
8. [Tab 2] Klik `[✕]`
9. [Tab 2] Verifikasi dialog `Unsaved Changes` tampil
10. [Tab 2] Klik `[Leave]`
11. [Tab 1] Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`. Kelas harness: multi-konteks (multi-tab), bagian 3 prinsip 13c. Spec serial.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Satu TC dalam spec sendiri: multi-tab tidak digabung dengan dua admin atau dua tenant (bagian 3 prinsip 13, cara menggabung antar-aksi); balapan Submit Create oleh dua admin (TC-GS-UCF-323 dan 89) ada di spec 029.
- Langkah penghubung (aksi tanpa `Verifikasi`): mengisi form pada dua tab sebelum `[Submit]`, membuka Global Settings > User > Custom Field di Tab 2, Search `Idem Probe {runId}-076` dan `(←)` yang menutupnya, serta menutup form dirty lewat `✕`, `Verifikasi` dialog `Unsaved Changes`, lalu `[Leave]` (S-08).
- Absence baris kedua memakai anchor positif: baris `Idem Probe {runId}-076` yang tampil pada Search yang sama dan error inline Tab 2 (butir 2 konvensi 8b).
- Pembagian TC lintas spec: TC-GS-UCF-89 dan 323 (balapan Create dua admin) ada di spec 029.
- Temuan untuk QA:
  - TC-GS-UCF-324 bertanda Manual Only (d) karena dua tab; kebutuhannya (dua tab pada satu sesi) ditulis di Prerequisites sesuai konvensi bagian 2.
  - TC-GS-UCF-324: Expected "tab kedua mendapat `Field name already exists`" tidak menyebut apakah error muncul saat mengetik atau saat Submit; spec mengasersi setelah `[Submit]` Tab 2. Tidak ada Post Condition.
