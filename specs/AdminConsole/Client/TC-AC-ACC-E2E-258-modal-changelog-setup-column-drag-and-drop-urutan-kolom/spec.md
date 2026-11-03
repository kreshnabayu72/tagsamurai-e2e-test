---
id: TC-AC-ACC-E2E-258-modal-changelog-setup-column-drag-and-drop-urutan-kolom
title: "Tiga Modal Changelog: Drag and Drop Urutan Kolom lalu Save dan Muat Ulang"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-744
coverage:
  web: automated
---

# Tiga Modal Changelog: Drag and Drop Urutan Kolom lalu Save dan Muat Ulang

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup (hanya dibaca): Client C-01 "PT Sejahtera Abadi" (Tab Subscription dan Tab Asset Control).
- Tabel "Modal Changelog" (parameter blok; kolom `Cara buka` selalu dimulai dari menu Client di sidebar):

| Modal | Cara buka | Urutan seret ke posisi pertama (berurutan) | Urutan header tersimpan setelah Save dan F5 |
|---|---|---|---|
| Changelog: Client | Klik menu Client di sidebar, lalu klik [Changelog] di toolbar List | Action, Client Name, Field, Old Value, New Value, Modified By, Date | Date, Modified By, New Value, Old Value, Field, Client Name, Action |
| Changelog: Subscription | Klik menu Client di sidebar, ketik Search "PT Sejahtera Abadi", tekan Enter, klik Company Name "PT Sejahtera Abadi", klik Tab Subscription, lalu klik [Changelog] | Action, Subscription, Field, Old Value, New Value, Modified By, Date | Date, Modified By, New Value, Old Value, Field, Subscription, Action |
| Changelog: Asset Control | Klik menu Client di sidebar, ketik Search "PT Sejahtera Abadi", tekan Enter, klik Company Name "PT Sejahtera Abadi", klik Tab Asset Control, lalu klik ikon Changelog | Action, Object, Field, Old Value, New Value, Modified By, Date | Date, Modified By, New Value, Old Value, Field, Object, Action |

- Kemampuan teknis: penghapusan preferensi kolom di browser untuk ketiga modal Changelog di hook `after` (Post Condition TC: urutan kolom kembali ke default lewat [Reset to Default] lalu [Save]; bagian 4 konvensi memakai penghapusan preferensi di browser), disediakan tim FE; konfigurasi kolom yang disimpan spec ini didaftarkan di `suite.md`.
- State global: preferensi kolom ketiga modal Changelog disimpan lalu dihapus di hook `after`; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman List dan Detail diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-ACC-744: Drag and drop urutan kolom tabel Changelog lalu Save dan refresh

1. Untuk setiap baris tabel "Modal Changelog" (langkah 1 sampai 7): buka modal sesuai kolom "Cara buka"
2. Klik header kolom Actions (⋯) pada tabel modal lalu klik "Setup Column..."
3. Untuk setiap kolom pada kolom "Urutan seret" baris itu (langkah 3 sampai 4): seret kolom itu ke posisi pertama daftar kolom
4. Verifikasi urutan header tabel di balik modal belum berubah dari sebelum seretan (urutan baru berlaku setelah [Save], D-008)
5. Klik [Save], tekan F5, lalu buka kembali modal yang sama sesuai kolom "Cara buka"
6. Verifikasi urutan header tersimpan sesuai kolom "Urutan header tersimpan" baris itu
7. Tutup modal Changelog

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): "Cara buka" tiap modal (menu Client di sidebar, Search dan buka Detail Client; hook suite hanya membuka List Client dan klik sidebar mereset Search), langkah 7 (menutup modal).
- Langkah 3 dan 4 diulang untuk 7 kolom pada tiap modal; ekspansi sekitar 3 x (modal + Setup Column + 14 + simpan + verifikasi + tutup) = sekitar 60 langkah.
- Spec ini melewati sekitar 35 langkah setelah ekspansi. Alasan: semua iterasi satu kelas harness (UI Only, Setup Column pada tiga modal Changelog dengan akun yang sama), parameter tiap iterasi ada di tabel Prerequisites, tanpa langkah bersyarat; tiap modal dibuka dari awal sehingga kegagalan satu modal tidak membuat modal lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-ACC-744 Expected a sampai c meminta urutan header di balik modal berubah langsung setelah tiap seretan, sebelum [Save]. Keputusan user 2026-11-02: spec mengikuti `docs/spec-decisions.md` D-008 (tabel di balik popup tidak berubah sampai [Save]): langkah 4 mengasersi urutan header belum berubah dan urutan baru diasersi setelah [Save] dan F5 (langkah 6). TC tidak diubah. TC tidak menyebut Preview Table di popup, sehingga spec tidak mengasersi preview.
  - TC-AC-ACC-744 langkah 3 menulis daftar seret termasuk "kolom ketiga" yang berbeda per modal (Client Name, Subscription, Object); spec menuliskannya pada tabel Prerequisites.
