---
id: TC-AC-ACC-E2E-081-edit-retry-activation-email-penerima-notifikasi-empat-sesi
title: "Notifikasi Kegagalan Activation Email: Total Control Menerima, Read Only, Group Manager, dan Active-Update-Only Tidak (Empat Sesi)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-977
coverage:
  web: automated
---

# Notifikasi Kegagalan Activation Email: Total Control Menerima, Read Only, Group Manager, dan Active-Update-Only Tidak (Empat Sesi)

## Prerequisites

- Mode: FE+BE. Kelas multi-konteks (c) dan harness eksternal (majukan waktu sistem, antrean percobaan ulang): empat sesi browser yang masing-masing menjadi objek asersi.
- Akun aktor: Sesi A Total Control Principal (A-01) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`; Sesi B Read Only Principal (A-02) `readOnlyPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_RO_PASSWORD`; Sesi C Group Manager Area Jakarta + descendant (A-03) `groupManagerJakarta_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_GM_PASSWORD`; Sesi D Active-Update-Only (A-06) `activeUpdateJakarta_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_ACTIVE_UPDATE_PASSWORD`. Keempat sesi login di hook `before` pada konteks browser terpisah dan membuka Admin Console > Client; hook `after` menutup Sesi B sampai D dan mengembalikan sesi ke akun default suite.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya.
- Kemampuan teknis: memajukan waktu sistem (jam server) dan memicu antrean percobaan ulang berjalan; jam browser tidak diubah karena antrean percobaan ulang dihitung di server dan tidak diamati lewat countdown UI (bagian 6 konvensi); jam server dipulihkan ke waktu nyata di hook `after` dan sebelum membuka Activity Log atau Changelog (S-09). Memaksa email service gagal (5xx) pada setiap percobaan kirim (disediakan tim FE/BE; endpoint tidak dikarang). Membaca jumlah notifikasi berstatus Unread dan item teratas pada dropdown notifikasi navbar.
- Sesi UI dan sesi API aktor tetap valid selama jam digeser (suite.md > Kemampuan teknis > Sesi tetap valid saat jam digeser).
- Dataset seed (nama bersuffix): Client `PT Notif Penerima {runId}-081` (replika C-FX12-10: Active, FAMS Active, Direct, Group Area Jakarta, Default User Not Yet Activated, Email awal `notifpenerima.awal+{runId}-081@qwertysystem.net`). Seeding Client lewat API/fixture BE di hook `before` (kemampuan disediakan tim FE/BE; endpoint tidak dikarang).
- Jeda percobaan ulang otomatis: 1 menit, 5 menit, 15 menit.
- Cleanup: hook `after` membatalkan simulasi kegagalan email service, menandai notifikasi uji `[Mark as Read]` di Sesi A, men-seed ulang Client dengan Email awal, dan memulihkan waktu sistem.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

1. [Sesi A, B, C, D] Masing-masing buka dropdown notifikasi pada navbar, catat jumlah notifikasi Unread (NA1, NB1, NC1, ND1), lalu tutup dropdown
2. Paksa email service gagal pada setiap percobaan kirim (5xx)
3. [Sesi A] Klik sub-tab Active
4. [Sesi A] Ketik Search `PT Notif Penerima {runId}-081`, tekan Enter
5. [Sesi A] Buka `⋯` baris `PT Notif Penerima {runId}-081` lalu klik `Edit`
6. [Sesi A] Ubah Email Default User menjadi `notifpenerima.baru+{runId}-081@qwertysystem.net`
7. [Sesi A] Klik `[Save]`
8. [Sesi A] Verifikasi toast sukses "Success, client has been updated."
9. Majukan waktu sistem 1 menit dan tunggu antrean percobaan ulang berjalan
10. Majukan waktu sistem 5 menit dan tunggu antrean percobaan ulang berjalan
11. Majukan waktu sistem 15 menit dan tunggu antrean percobaan ulang berjalan
12. [Sesi A] Muat ulang Admin Console > Client, buka dropdown notifikasi, catat jumlah Unread (NA2), dan lihat item teratas
13. [Sesi A] Verifikasi NA2 sama dengan NA1 + 1
14. [Sesi A] Verifikasi item teratas berstatus Unread dengan Title "Activation email not delivered" dan Body "PT Notif Penerima {runId}-081: the activation email could not be sent after repeated attempts."
15. [Sesi A] Verifikasi tombol aksi item teratas hanya `[Mark as Read]` (tidak ada `[Detail]`)
16. [Sesi B] Muat ulang Admin Console > Client, buka dropdown notifikasi, catat jumlah Unread (NB2), dan lihat daftar item
17. [Sesi B] Verifikasi NB2 sama dengan NB1
18. [Sesi B] Verifikasi tidak ada item Title "Activation email not delivered" dengan Body "PT Notif Penerima {runId}-081: the activation email could not be sent after repeated attempts." di dropdown
19. [Sesi C] Muat ulang Admin Console > Client, buka dropdown notifikasi, catat jumlah Unread (NC2), dan lihat daftar item
20. [Sesi C] Verifikasi NC2 sama dengan NC1
21. [Sesi C] Verifikasi tidak ada item Title "Activation email not delivered" dengan Body "PT Notif Penerima {runId}-081: the activation email could not be sent after repeated attempts." di dropdown
22. [Sesi D] Muat ulang Admin Console > Client, buka dropdown notifikasi, catat jumlah Unread (ND2), dan lihat daftar item
23. [Sesi D] Verifikasi ND2 sama dengan ND1
24. [Sesi D] Verifikasi tidak ada item Title "Activation email not delivered" dengan Body "PT Notif Penerima {runId}-081: the activation email could not be sent after repeated attempts." di dropdown
25. [Sesi A] Klik `[Mark as Read]` pada notifikasi uji lalu pulihkan waktu sistem ke waktu nyata

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Alasan di atas 35 langkah (sekitar 30 langkah): satu TC yang inheren memakai empat sesi dan majukan waktu sistem; sesi B sampai D adalah objek asersi (absence notifikasi), bukan pengamat pasif, sehingga bukan `P-6`.
- Asersi absence Sesi B sampai D (butir 8b-2) didahului pencatatan jumlah Unread dan pembukaan dropdown pada surface yang sama (daftar item termuat); Sesi A memberi anchor positif bahwa notifikasi sudah terbit pada waktu yang sama.
- Temuan untuk QA:
  - TC-977 bertanda Manual Only (memajukan waktu sistem); empat sesi login paralel disediakan tim FE.
  - Asersi "tidak ada item" untuk Read Only, Group Manager, dan Active-Update-Only tidak menyebut bahwa dropdown boleh memuat notifikasi lain; spec memeriksa Title dan Body spesifik serta jumlah Unread tetap.
