---
id: TC-AC-PF-E2E-125-aksi-ditolak-tidak-menulis-entri-log-di-surface-mana-pun
title: "Absence Log: Aksi yang Ditolak Validasi atau Guard Tidak Menulis Entri di Changelog, Activity Log, dan System Log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-538
coverage:
  web: automated
---

# Absence Log: Aksi yang Ditolak Validasi atau Guard Tidak Menulis Entri di Changelog, Activity Log, dan System Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active).
- Data Pre-setup (hanya dibaca, tidak diubah): Dataset Plan G (Pre-setup #27): custom plan `Guard Active` dengan satu client Active (`PT Guard Active`), dan Dataset Plan C (Pre-setup #23): custom plan `Growth Tier` v20 (nama dipakai sebagai nama duplikat). Aksi dalam spec ini selalu ditolak sehingga data Pre-setup dan Last Modified tidak berubah. Pengecualian S-06/S-12 butir A-14 dipakai (nama literal tanpa suffix pada data Pre-setup, hanya dibaca).
- Baseline: jumlah entri Changelog tab Custom, jumlah entri Activity Log (Filter Object `Plans & Features`), dan jumlah entri System Log aktor dicatat pada langkah 2 lewat kemampuan baca (audit trail permanen; S-12, bagian 8b butir 10).
- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca jumlah entri Changelog tab Custom, Activity Log, dan System Log aktor. Tidak ada state global yang diubah; hook `after` tidak memerlukan pemulihan Dataset.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nama data Pre-setup pada langkah mengikuti Tabel Data Uji TC dan dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.

## Test Steps

### TC-AC-PF-538: Aksi ditolak tidak menulis entri log

1. Klik tab `Custom` sub-tab `Active`
2. Catat jumlah entri Changelog tab Custom, Activity Log (Filter Object `Plans & Features`), dan System Log aktor sebagai baseline
3. Buka Overlay Row Action `Guard Active`, lalu klik `Archive`
4. Verifikasi Dialog `Cannot Archive Plan` tampil
5. Klik `[OK]`
6. Klik `+ Custom Plan` pada toolbar
7. Pilih Product `FAMS`, pilih Template `Growth`, isi Plan Name `Growth Tier`
8. Klik `[Submit]`
9. Verifikasi Pesan `Plan name already exists` tampil dan pembuatan ditolak
10. Klik segmen Breadcrumb `Plans & Features` pada form Create Custom Plan
11. Verifikasi Dialog `Unsaved Changes` tampil
12. Klik `[Leave]`
13. Klik tab `Custom` sub-tab `Active`
14. Klik ikon Changelog pada toolbar tab Custom
15. Verifikasi Modal Changelog tab Custom tampil dengan entri sebelumnya (anchor)
16. Verifikasi Jumlah entri Changelog tab Custom sama dengan baseline langkah 2 (tidak ada entri Archive `Guard Active` dan tidak ada entri Create `Growth Tier` baru)
17. Tutup modal Changelog
18. Buka Admin Console > Activity Log, lalu filter Object `Plans & Features`
19. Verifikasi Activity Log menampilkan entri Object `Plans & Features` yang sudah ada (anchor)
20. Verifikasi Jumlah entri Activity Log sama dengan baseline langkah 2 (tidak ada entri dari kedua percobaan)
21. Buka menu Global Settings > User, cari `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net`, buka Detail User `Andi Wijaya`, lalu klik Tab System Log
22. Verifikasi System Log aktor menampilkan entri yang sudah ada (anchor)
23. Verifikasi Jumlah entri System Log aktor sama dengan baseline langkah 2 (tidak ada entri dari kedua percobaan)

## Notes

- Langkah penghubung (S-03): klik tab dan sub-tab sebagai precondition TC (langkah 1), penutupan form dirty lewat klik segmen Breadcrumb `Plans & Features`, `Unsaved Changes`, dan `[Leave]` (S-08; langkah 10 sampai 12), klik tab `Custom` sub-tab `Active` sesudah breadcrumb yang mendarat di Default > Active (langkah 13), tutup modal Changelog (langkah 17), serta navigasi menu dan Search untuk menemukan user target (R-16; langkah 18 dan 21).
- Spec absence (kelas g): kedua pemicu (Archive ditolak guard, Create ditolak nama duplikat) adalah aksi nyata untuk TC-AC-PF-538 dengan baseline sendiri (S-05, S-12). Asersi "tidak ada entri baru" pada TC lain di suite ini ditulis sebagai asersi jumlah terhadap baseline di spec asalnya dan tidak dirujuk ke spec ini.
- Temuan untuk QA:
  - TC-AC-PF-538 langkah 2 ("Coba Create custom plan dengan nama duplikat `Growth Tier` sehingga ditolak") tidak menyebut bentuk penolakan; spec memakai pesan `Plan name already exists` sesuai TC-AC-PF-259 sebagai anchor penolakan.
  - TC-AC-PF-538 tidak menyebut cara menutup form Create sesudah penolakan; spec memakai klik segmen Breadcrumb `Plans & Features`, dialog `Unsaved Changes`, dan `[Leave]` (S-08).
  - TC-AC-PF-538 tidak menyebut cara membaca jumlah entri Activity Log dan System Log aktor; spec memakai kemampuan baca yang disediakan tim FE/BE tanpa endpoint karangan.
  - Post Condition "Tidak ada entri baru" diasersi lewat langkah 16, 20, dan 23.
