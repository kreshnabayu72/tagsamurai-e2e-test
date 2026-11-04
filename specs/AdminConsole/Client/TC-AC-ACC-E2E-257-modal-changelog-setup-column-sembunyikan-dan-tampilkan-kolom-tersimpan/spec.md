---
id: TC-AC-ACC-E2E-257-modal-changelog-setup-column-sembunyikan-dan-tampilkan-kolom-tersimpan
title: "Tiga Modal Changelog: Ceklis dan Unceklis Kolom lalu Save, Muat Ulang, dan Tampilkan Kembali"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-743
coverage:
  web: automated
---

# Tiga Modal Changelog: Ceklis dan Unceklis Kolom lalu Save, Muat Ulang, dan Tampilkan Kembali

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup (hanya dibaca): Client C-01 "PT Sejahtera Abadi" (Tab Subscription dan Tab Asset Control).
- Tabel "Modal Changelog" (parameter blok; kolom `Cara buka` selalu dimulai dari menu Client di sidebar):

| Modal | Cara buka | Kolom Hideable (default tercentang, satu kolom per putaran) |
|---|---|---|
| Changelog: Client | Klik menu Client di sidebar, lalu klik [Changelog] di toolbar List | Date, Action, Client Name, Field, Old Value, New Value, Modified By |
| Changelog: Subscription | Klik menu Client di sidebar, ketik Search "PT Sejahtera Abadi", tekan Enter, klik Company Name "PT Sejahtera Abadi", klik Tab Subscription, lalu klik [Changelog] | Date, Action, Subscription, Field, Old Value, New Value, Modified By |
| Changelog: Asset Control | Klik menu Client di sidebar, ketik Search "PT Sejahtera Abadi", tekan Enter, klik Company Name "PT Sejahtera Abadi", klik Tab Asset Control, lalu klik ikon Changelog | Date, Action, Object, Field, Old Value, New Value, Modified By |

- Kemampuan teknis: penghapusan preferensi kolom di browser untuk ketiga modal Changelog di hook `after` (Post Condition TC: konfigurasi kolom kembali ke default lewat [Reset to Default] lalu [Save]; bagian 4 konvensi memakai penghapusan preferensi di browser), disediakan tim FE; konfigurasi kolom yang disimpan spec ini didaftarkan di `suite.md`.
- State global: preferensi kolom ketiga modal Changelog disimpan lalu dihapus di hook `after`; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman List dan Detail diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-ACC-743: Ceklis dan unceklis kolom tabel Changelog lalu Save dan refresh

1. Untuk setiap baris tabel "Modal Changelog" (langkah 1 sampai 11): buka modal sesuai kolom "Cara buka"
2. Untuk setiap kolom pada kolom "Kolom Hideable" baris itu (langkah 2 sampai 10): klik header kolom Actions (⋯) pada tabel modal lalu klik "Setup Column..."
3. Hapus centang kolom itu
4. Verifikasi kolom masih tampil di tabel di balik modal setelah centang dilepas, sebelum [Save] (perubahan baru berlaku setelah [Save], D-065)
5. Klik [Save], tekan F5, lalu buka kembali modal yang sama sesuai kolom "Cara buka"
6. Verifikasi kolom tetap hilang setelah [Save], F5, dan pembukaan ulang modal
7. Klik header kolom Actions (⋯) pada tabel modal lalu klik "Setup Column..."
8. Centang kembali kolom itu, lalu klik [Save]
9. Verifikasi kolom tampil kembali setelah dicentang dan [Save]
10. (akhir putaran kolom; ulangi langkah 2 sampai 9 untuk kolom berikutnya pada modal yang sama)
11. Tutup modal Changelog

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): "Cara buka" tiap modal (menu Client di sidebar, Search dan buka Detail Client; hook suite hanya membuka List Client dan klik sidebar mereset Search), langkah 11 (menutup modal).
- Langkah 2 sampai 9 diulang untuk 7 kolom pada tiap modal (8 langkah x 7 x 3 = 168 langkah setelah ekspansi, ditambah pembukaan modal dan penutupan).
- Spec ini melewati sekitar 35 langkah setelah ekspansi. Alasan: semua iterasi satu kelas harness (UI Only, Setup Column pada tiga modal Changelog dengan akun yang sama), parameter tiap iterasi ada di tabel Prerequisites, tanpa langkah bersyarat, dan tiap kolom dikembalikan ke tampil di akhir putaran sehingga kegagalan satu putaran tidak membuat putaran lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-ACC-743: TC sudah diselaraskan pada 2026-11-03 sesuai `docs/spec-decisions.md` D-065 (tabel di balik popup tidak berubah sampai [Save]); spec dan TC sama. langkah 4 mengasersi kolom masih tampil sebelum [Save] dan hilangnya kolom diasersi setelah [Save] (langkah 6). TC tidak menyebut Preview Table di popup, sehingga spec tidak mengasersi preview. Sisa konflik hanya `prd-conventions.md` §9.3 (di luar scope suite, dilaporkan ke pemilik foundation).
  - TC-AC-ACC-743 Expected memuat sembilan kelas Hideable (Client Name hanya di Changelog: Client, Subscription hanya di Changelog: Subscription, Object hanya di Changelog: Asset Control); spec mengikuti pemetaan per modal pada tabel Prerequisites.
