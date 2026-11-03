---
id: TC-AC-ACC-E2E-259-modal-changelog-setup-column-pin-dan-unpin-kolom
title: "Tiga Modal Changelog: Pin dan Unpin Kolom Membekukan Kolom saat Scroll Horizontal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-745
coverage:
  web: automated
---

# Tiga Modal Changelog: Pin dan Unpin Kolom Membekukan Kolom saat Scroll Horizontal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup (hanya dibaca): Client C-01 "PT Sejahtera Abadi" (Tab Subscription dan Tab Asset Control).
- Tabel "Modal Changelog" (parameter blok; kolom `Cara buka` selalu dimulai dari menu Client di sidebar):

| Modal | Cara buka | Kolom Hideable (satu kolom per putaran) |
|---|---|---|
| Changelog: Client | Klik menu Client di sidebar, lalu klik [Changelog] di toolbar List | Date, Action, Client Name, Field, Old Value, New Value, Modified By |
| Changelog: Subscription | Klik menu Client di sidebar, ketik Search "PT Sejahtera Abadi", tekan Enter, klik Company Name "PT Sejahtera Abadi", klik Tab Subscription, lalu klik [Changelog] | Date, Action, Subscription, Field, Old Value, New Value, Modified By |
| Changelog: Asset Control | Klik menu Client di sidebar, ketik Search "PT Sejahtera Abadi", tekan Enter, klik Company Name "PT Sejahtera Abadi", klik Tab Asset Control, lalu klik ikon Changelog | Date, Action, Object, Field, Old Value, New Value, Modified By |

- Kemampuan teknis: pengubahan ukuran jendela browser hingga tabel modal memiliki scroll horizontal, dengan pemulihan ukuran jendela di langkah penghubung; penghapusan preferensi kolom di browser untuk ketiga modal Changelog di hook `after` (Post Condition TC: tidak ada kolom terpin; bagian 4 konvensi memakai penghapusan preferensi di browser), disediakan tim FE; konfigurasi kolom yang disimpan spec ini didaftarkan di `suite.md`.
- State global: preferensi kolom ketiga modal Changelog disimpan lalu dihapus di hook `after`; ukuran jendela dipulihkan; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman List dan Detail diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-ACC-745: Pin dan unpin kolom tabel Changelog membekukan kolom saat scroll horizontal

1. Untuk setiap baris tabel "Modal Changelog" (langkah 1 sampai 12): buka modal sesuai kolom "Cara buka"
2. Untuk setiap kolom pada kolom "Kolom Hideable" baris itu (langkah 2 sampai 10): klik header kolom Actions (⋯) pada tabel modal lalu klik "Setup Column..."
3. Klik ikon Pin pada kolom itu lalu klik [Save]
4. Perkecil lebar jendela hingga tabel modal memiliki scroll horizontal, lalu scroll tabel ke kanan
5. Verifikasi kolom itu tetap terlihat di sisi kiri tabel saat tabel di-scroll ke kanan
6. Tekan F5, buka kembali modal yang sama sesuai kolom "Cara buka", lalu scroll tabel ke kanan
7. Verifikasi kolom itu tetap terlihat di sisi kiri tabel setelah F5
8. Klik header kolom Actions (⋯) pada tabel modal lalu klik "Setup Column...", unpin kolom itu, lalu klik [Save]
9. Scroll tabel ke kanan
10. Verifikasi kolom itu ikut bergeser bersama kolom lain setelah di-unpin
11. Pulihkan ukuran jendela ke ukuran awal
12. Tutup modal Changelog (akhir putaran terakhir tiap modal)

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16, S-09): "Cara buka" tiap modal (menu Client di sidebar, Search dan buka Detail Client; hook suite hanya membuka List Client dan klik sidebar mereset Search), langkah 11 (memulihkan ukuran jendela), langkah 12 (menutup modal).
- Langkah 2 sampai 10 diulang untuk 7 kolom pada tiap modal (9 langkah x 7 x 3 = 189 langkah setelah ekspansi, ditambah pembukaan modal, pemulihan jendela, dan penutupan).
- Spec ini melewati sekitar 35 langkah setelah ekspansi. Alasan: semua iterasi satu kelas harness (UI Only, Setup Column pada tiga modal Changelog dengan akun yang sama), parameter tiap iterasi ada di tabel Prerequisites, tanpa langkah bersyarat, dan tiap kolom dikembalikan ke tidak terpin di akhir putaran sehingga kegagalan satu putaran tidak membuat putaran lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-ACC-745 langkah 4 tidak menyebut lebar jendela yang memunculkan scroll horizontal; spec memperkecil lebar sampai tabel memiliki scroll horizontal.
  - Hubungan Pin dengan Hideable: TC tidak menyebut kolom yang tidak dapat dipin; spec mengikuti Expected sembilan anggota kelas Hideable.
