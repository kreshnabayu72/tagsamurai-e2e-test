---
id: TC-GS-ROLE-E2E-026-popup-assign-filter-panel
title: "Popup Assign: Filter Panel Position, Division, Status, Activation Status, Temporary User, Temporary Until, dan Custom Field"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-73
  - TC-GS-ROLE-74
coverage:
  web: automated
---

# Popup Assign: Filter Panel Position, Division, Status, Activation Status, Temporary User, Temporary Until, dan Custom Field

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data; popup hanya dibuka dan difilter.
- Akun: Ahmad Fauzi (Total Control), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD` (Pre-setup #1). Login dan navigasi dilakukan sekali di hook `before`. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Data Pre-setup (hanya dibaca): kandidat picker Pre-setup #11 (Maya Anggraini Staff IT Inactive; Ahmad Fauzan Warehouse Staff Logistics; Rudi Hartono Pending Activation) dan Pre-setup #18. Pool memuat user dengan Position, Division, dan Status yang berbeda-beda (sedikitnya dua nilai distinct per kolom).
- Data uji field yang kolomnya Hidden di picker (disediakan tim FE): user temporary di pool (`{user temporary uji}`, Temporary User Yes, Temporary Until `{tanggal temporary until}`), dan user ber-Region Bandung (`{user region bandung}`) pada Custom Field aktif Region. Rentang Temporary Until memuat tepat `{tanggal temporary until}`. Format tanggal mengikuti General Settings aktif.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Hook `beforeEach`: membuka Global Settings > Role & Permission > Tab Total Control.
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: memilih rentang tanggal pada date range picker Filter Panel; memilih opsi pada multi-select searchable.

Field Filter yang diuji (langkah 6 sampai 11 untuk TC-GS-ROLE-73; langkah 16 sampai 21 untuk TC-GS-ROLE-74):

| Field | Nilai dipilih | Baris pembanding yang harus tampil | Aturan hasil |
|---|---|---|---|
| Position | `Staff` | Maya Anggraini | setiap baris yang tampil ber-Position Staff |
| Division | `Logistics` | Ahmad Fauzan (Warehouse Staff) | tabel hanya memuat Ahmad Fauzan (Warehouse Staff) |
| Status | `Inactive` | Maya Anggraini | setiap baris yang tampil ber-Status Inactive |
| Activation Status | `Pending Activation` | Rudi Hartono | tabel hanya memuat Rudi Hartono |
| Temporary User | `Yes` | `{user temporary uji}` | tabel hanya memuat user temporary (`{user temporary uji}`) |
| Temporary Until | rentang `{tanggal temporary until}` sampai `{tanggal temporary until}` | `{user temporary uji}` | tabel hanya memuat user dengan Temporary Until dalam rentang |
| Region (Custom Field aktif) | `Bandung` | `{user region bandung}` | tabel hanya memuat user ber-Region Bandung |

## Test Steps

### TC-GS-ROLE-73: Filter Popup Assign berdasarkan Position, Division, dan Status

1. Klik `[+ Assign]`
2. Klik icon Filter
3. Verifikasi field `Position` (placeholder `All positions`) bertipe multi-select searchable
4. Verifikasi field `Division` (placeholder `All divisions`) bertipe multi-select searchable
5. Verifikasi field `Status` (placeholder `All statuses`) bertipe multi-select searchable
6. Untuk setiap field Position, Division, dan Status pada tabel Prerequisites (langkah 6 sampai 11), klik `[Clear Field]` (Reset)
7. Pilih nilai field sesuai tabel
8. Klik `[Apply]`
9. Verifikasi baris pembanding pada tabel tampil
10. Verifikasi tabel memenuhi kolom "Aturan hasil" pada tabel
11. Klik icon Filter

### TC-GS-ROLE-74: Filter Popup Assign berdasarkan Activation Status, Temporary User, Temporary Until, dan Custom Field

12. Verifikasi field `Activation Status` (placeholder `All statuses`) bertipe multi-select searchable
13. Verifikasi field `Temporary User` (placeholder `All options`) tampil
14. Verifikasi field `Temporary Until` (placeholder `Select date`) bertipe date range picker
15. Verifikasi field `Region` (Custom Field aktif) tampil
16. Untuk setiap field Activation Status, Temporary User, Temporary Until, dan Region pada tabel Prerequisites (langkah 16 sampai 21), klik `[Clear Field]` (Reset)
17. Pilih nilai field sesuai tabel
18. Klik `[Apply]`
19. Verifikasi baris pembanding pada tabel tampil
20. Verifikasi tabel memenuhi kolom "Aturan hasil" pada tabel
21. Klik icon Filter

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Mode: FE+BE.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (73, 74) dipertahankan.
- Blok langkah 6 sampai 11 diulang tiga kali (Position, Division, Status) dan blok langkah 16 sampai 21 diulang empat kali (Activation Status, Temporary User, Temporary Until, Region); parameter tiap iterasi ada di tabel Prerequisites, tanpa langkah bersyarat. Jumlah langkah dengan ekspansi 51: langkah 1 sampai 5 (5), blok TC-GS-ROLE-73 (3 x 6 = 18), langkah 12 sampai 15 (4), dan blok TC-GS-ROLE-74 (4 x 6 = 24).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC sumber): klik `[Clear Field]` di awal tiap iterasi (padanan "Reset" pada TC-GS-ROLE-73), dan klik icon Filter di akhir tiap iterasi untuk membuka kembali Filter Panel (Filter Panel menutup setelah `[Apply]`, pola sama dengan Filter Panel tabel Division). Pada iterasi terakhir langkah 21, panel Filter dibiarkan terbuka dan ditutup oleh hook `beforeEach` berikutnya.
- Spec melewati sekitar 35 langkah (51 langkah dengan ekspansi) karena tujuh field Filter Panel Popup Assign diuji satu per satu dengan blok identik. Semua blok satu kelas harness (fungsional), satu popup dan satu dataset; tiap iterasi diawali `[Clear Field]` sehingga kegagalan satu field tidak membuat field lain kehilangan makna.
- Asersi universal ("setiap baris", "hanya") didahului `Verifikasi` baris pembanding pada surface yang sama (langkah 9 dan 19).
- Pembagian TC lintas spec: TC-GS-ROLE-51, 52, 53, 77 ada di spec 023; TC-GS-ROLE-54 sampai 57 ada di spec 024; TC-GS-ROLE-69 sampai 72 ada di spec 025; TC-GS-ROLE-75, 76, 293 ada di spec 027.
- Temuan untuk QA:
  - TC-GS-ROLE-73 langkah 4 dan 5 menulis "Reset" tanpa menyebut label tombol; spec memakai `[Clear Field]` mengikuti pola Filter Panel.
  - TC-GS-ROLE-74 langkah 2 hanya membuka Filter; langkah pilih nilai dan `[Apply]` tidak ada di TC, sehingga spec menambahkannya berdasarkan Expected a sampai d.
  - TC-GS-ROLE-74 Expected a ("hanya Rudi Hartono") bertentangan dengan Pre-setup #18: Yoga Pratama (Pending Activation) ada di pool kandidat. Spec mengikuti TC; bila Yoga Pratama berada di pool, langkah 20 untuk Activation Status gagal.
  - TC-GS-ROLE-74 tidak menyebut user temporary, nilai Temporary Until, maupun user ber-Region Bandung; data disediakan tim FE (Pre-setup #19 hanya mencakup user yang sudah ber-access level).
  - TC-GS-ROLE-74 Expected tidak menyebut placeholder field Region; spec hanya memverifikasi field tampil.
  - Kolom Temporary User dan Region Hidden di picker, sehingga aturan hasil memakai daftar nama dari data uji, bukan membaca kolom.
