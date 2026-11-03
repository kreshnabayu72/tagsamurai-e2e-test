---
id: TC-AC-PF-E2E-074-create-default-plan-open-api-off-dan-open-api-on-dengan
title: "Create Default Plan: Open API OFF Mengunci API Call Quota dan Open API ON Tanpa Quota Ditolak"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-751
  - TC-AC-PF-752
coverage:
  web: automated
---

# Create Default Plan: Open API OFF Mengunci API Call Quota dan Open API ON Tanpa Quota Ditolak

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Andi Wijaya`; Global Role Manage plans & licensing Create, Read, Update, Delete), password dari `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman Plans & Licensing > Plans & Features (Default > Active) dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (nilai awal akun aktor); spec ini tidak mengubahnya.
- Data Pre-setup: Dataset Plan S (Default SAMS: `Supply Starter` Free dan `Supply Pro` Paid; slot Paid tersisa; payload fitur FAMS sebagai placeholder). Spec ini tidak menyimpan plan baru.
- Data Dinamis: `Supply Quota Kosong {runId}-074` (Plan Name pada TC-AC-PF-752; ditolak validasi sehingga tidak tersimpan dan dicari di Search untuk memastikan tidak ada).
- Kemampuan teknis: fixture BE untuk menyemai dan memulihkan Dataset Pre-setup (idempoten, disediakan tim FE/BE). Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data dirujuk sebagai `Fixture.plansFeatures.<kunci>` dan ditandai di sini sebagai fixture yang belum ada.
- Pengecualian S-06/S-12 butir A-14: Dataset Pre-setup berslot terbatas (1 Free dan 3 Paid per Product) dan nama literal yang menentukan asersi dipakai tanpa suffix; pemulihan Dataset ke keadaan awal oleh fixture BE dijalankan di hook `before` dan `after` serta sebagai langkah penghubung yang tertulis pada Test Steps; data yang dibuat spec ini bersuffix `{runId}-074`.
- State global: Dataset Pre-setup bersama dipulihkan sebagaimana di atas dan suite berjalan serial (`parallel: false`, lihat `suite.md`). Tiap plan yang dibuat spec ini menambah entri Changelog permanen dan mengubah Last Updated tabel List; entri tidak dapat dihapus lewat UI dan tidak diasersi spec ini.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): fixture BE menghapus plan yang dibuat spec dan memulihkan Dataset.

## Test Steps

### TC-AC-PF-751: Create Default Plan: Open API OFF mengunci API call quota ke — dengan tooltip penjelas, toggle ON membuka field

1. Klik `+ Default Plan`
2. Pilih Product `SAMS` dan Pricing Type `Paid`
3. Amati toggle Open API dan field API call quota pada nilai awal
4. Verifikasi nilai awal toggle Open API OFF
5. Verifikasi nilai awal API call quota `—` Disabled (tetap tampil)
6. Nyalakan toggle Open API lalu pilih API call quota `100K/month`
7. Matikan toggle Open API
8. Verifikasi API call quota otomatis reset ke `—`
9. Verifikasi field API call quota terkunci (Disabled, tetap tampil)
10. Hover field API call quota
11. Verifikasi tooltip `Turn on Open API to set an API call quota.`
12. Nyalakan toggle Open API lagi
13. Verifikasi field API call quota aktif kembali
14. Verifikasi tooltip hilang
15. Klik `[Clear Field]`

### TC-AC-PF-752: Create Default Plan: Open API ON dengan API call quota kosong ditolak dengan pesan inline pada field API call quota

16. Pilih Product `SAMS`, Pricing Type `Paid`, dan isi Plan Name `Supply Quota Kosong {runId}-074`
17. Nyalakan toggle Open API tanpa memilih API call quota
18. Klik `[Submit]`
19. Verifikasi pesan inline `API call quota must not be empty` di bawah field API call quota
20. Verifikasi form tetap terbuka dengan input dipertahankan
21. Verifikasi tidak ada toast sukses
22. Klik segmen `Plans & Features` pada breadcrumb
23. Verifikasi dialog `Unsaved Changes` tampil
24. Klik `[Leave]`
25. Verifikasi halaman Plans & Licensing > Plans & Features > Default > Active tampil
26. Ketik Search `Supply Quota Kosong {runId}-074`, tekan Enter
27. Verifikasi empty state "No results found" (tidak ada plan baru)
28. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03, S-09): `[Clear Field]` pada langkah 15 mengembalikan form ke keadaan bersih sebelum blok TC-AC-PF-752; `(←)` pada kotak Search di akhir menutup input dan mereset tabel. Menutup form dirty ditulis deterministik: breadcrumb, `Verifikasi` dialog `Unsaved Changes`, `[Leave]` (S-08); halaman Default > Active pada langkah 25 adalah tujuan setelah `[Leave]` dan menjadi anchor permukaan sebelum Search.
- Search pada langkah 26 mengikuti Langkah TC (bukan untuk menemukan baris target); empty state "No results found" hasil Search adalah anchor positif yang sah untuk absence hasil pencarian (bagian 8b butir 2).
- Temuan untuk QA:
-   - Post Condition TC yang tidak punya langkah observasi di TC (mis. `Tidak ada perubahan data`, `Default plan ... tersimpan`) tidak diasersi.
-   - TC-AC-PF-751 Expected d menulis "tooltip hilang" tanpa menyebut posisi kursor saat diamati; spec mengasersinya segera setelah toggle dinyalakan.
