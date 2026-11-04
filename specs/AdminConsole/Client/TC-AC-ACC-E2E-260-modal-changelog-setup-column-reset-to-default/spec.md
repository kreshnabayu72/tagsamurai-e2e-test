---
id: TC-AC-ACC-E2E-260-modal-changelog-setup-column-reset-to-default
title: "Tiga Modal Changelog: Reset to Default pada Modal Setup Column"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-746
coverage:
  web: automated
---

# Tiga Modal Changelog: Reset to Default pada Modal Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup (hanya dibaca): Client C-01 "PT Sejahtera Abadi" (Tab Subscription dan Tab Asset Control).
- Tabel "Modal Changelog" (parameter blok; kolom `Cara buka` selalu dimulai dari menu Client di sidebar):

| Modal | Cara buka | Urutan default setelah Reset (7 kolom tercentang, tanpa kolom terpin) |
|---|---|---|
| Changelog: Client | Klik menu Client di sidebar, lalu klik [Changelog] di toolbar List | Date, Action, Client Name, Field, Old Value, New Value, Modified By |
| Changelog: Subscription | Klik menu Client di sidebar, ketik Search "PT Sejahtera Abadi", tekan Enter, klik Company Name "PT Sejahtera Abadi", klik Tab Subscription, lalu klik [Changelog] | Date, Action, Subscription, Field, Old Value, New Value, Modified By |
| Changelog: Asset Control | Klik menu Client di sidebar, ketik Search "PT Sejahtera Abadi", tekan Enter, klik Company Name "PT Sejahtera Abadi", klik Tab Asset Control, lalu klik ikon Changelog | Date, Action, Object, Field, Old Value, New Value, Modified By |

- Kemampuan teknis: penghapusan preferensi kolom di browser untuk ketiga modal Changelog di hook `after` (bagian 4 konvensi), disediakan tim FE; konfigurasi kolom yang disimpan spec ini didaftarkan di `suite.md`.
- State global: preferensi kolom ketiga modal Changelog disimpan lalu dihapus di hook `after`; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman List dan Detail diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-ACC-746: Reset to Default pada modal Setup Column tabel Changelog

1. Untuk setiap baris tabel "Modal Changelog" (langkah 1 sampai 10): buka modal sesuai kolom "Cara buka"
2. Klik header kolom Actions (⋯) pada tabel modal lalu klik "Setup Column..."
3. Hapus centang Field, seret Date ke posisi terakhir, klik ikon Pin pada Action, lalu klik [Save]
4. Klik header kolom Actions (⋯) pada tabel modal lalu klik "Setup Column..." lalu klik [Reset to Default]
5. Verifikasi daftar kolom: 7 kolom tercentang dengan urutan default pada kolom tabel "Urutan default setelah Reset"
6. Verifikasi tidak ada kolom terpin
7. Verifikasi tabel di balik modal masih menampilkan konfigurasi kustom hasil langkah 3 (kolom Field tidak tampil) sebelum [Save] (Reset baru berlaku setelah [Save], D-065)
8. Klik [Save], tekan F5, lalu buka kembali modal yang sama sesuai kolom "Cara buka"
9. Verifikasi konfigurasi default tersimpan setelah [Save] dan F5 (7 kolom dengan urutan default, tanpa kolom terpin)
10. Tutup modal Changelog

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): "Cara buka" tiap modal (menu Client di sidebar, Search dan buka Detail Client; hook suite hanya membuka List Client dan klik sidebar mereset Search), langkah 10 (menutup modal).
- Langkah 1 sampai 10 diulang untuk 3 modal (30 langkah setelah ekspansi, 10 langkah nominal bila Cara buka dihitung satu).
- Spec ini mendekati sekitar 35 langkah setelah ekspansi; semua iterasi satu kelas harness (UI Only) dengan akun yang sama dan tiap modal dibuka dari awal.
- Temuan untuk QA:
  - TC-AC-ACC-746: TC sudah diselaraskan pada 2026-11-03 sesuai `docs/spec-decisions.md` D-065 (tabel di balik popup tidak berubah sampai [Save]); spec dan TC sama. daftar kolom di popup diasersi langkah 5 dan 6, langkah 7 mengasersi tabel di balik modal masih memakai konfigurasi kustom, dan konfigurasi default diasersi setelah [Save] dan F5 (langkah 9). TC tidak menyebut Preview Table di popup, sehingga spec tidak mengasersi preview. Sisa konflik hanya `prd-conventions.md` §9.3 (di luar scope suite, dilaporkan ke pemilik foundation).
