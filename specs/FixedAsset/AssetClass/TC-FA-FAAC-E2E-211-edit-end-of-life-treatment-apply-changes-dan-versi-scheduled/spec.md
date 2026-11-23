---
id: TC-FA-FAAC-E2E-211-edit-end-of-life-treatment-apply-changes-dan-versi-scheduled
title: "Edit End-of-Life Treatment pada Asset Class yang Dipakai Aset: Apply Changes Membentuk Versi Berlaku dan Effective From Masa Depan Menjadwalkan Versi"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-724
  - TC-FA-FAAC-726
sourceRules: ["FAAC-LOGIC-02h", "FLD-33", "FAAC-LOGIC-07", "FAAC-LOGIC-07a", "FAAC-LOGIC-07f", "FAAC-LOGIC-07d", "F-FAAC-02.k5", "F-FAAC-02.k15", "F-FAAC-02.k18", "F-FAAC-02.k19", "L-03", "L-12", "D-11", "E-FAAC-112", "E-FAAC-113"]
smoke: []
dependsOn: []
trace:
  "FAAC-LOGIC-02h": [17, 22, 36]
  "FLD-33": [17, 22, 36]
  "FAAC-LOGIC-07": [7, 8, 9, 10]
  "FAAC-LOGIC-07a": [10]
  "FAAC-LOGIC-07f": [8]
  "FAAC-LOGIC-07d": [32, 33, 34]
  "F-FAAC-02.k5": [12, 13]
  "F-FAAC-02.k15": [32, 33]
  "F-FAAC-02.k18": [17, 22]
  "F-FAAC-02.k19": [34]
  "L-03": [22]
  "L-12": [40]
  "D-11": [7]
  "E-FAAC-112": [7, 13]
  "E-FAAC-113": [34, 40]
coverage:
  web: automated
---

# Edit End-of-Life Treatment pada Asset Class yang Dipakai Aset: Apply Changes Membentuk Versi Berlaku dan Effective From Masa Depan Menjadwalkan Versi

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Nama tampil akun pada kolom Modified By: `Rina W` (format [First Name] [Last Initial], menurut TC-541 sampai TC-550). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup bernama literal (seed idempotent, dipulihkan ke nilai awal oleh fixture BE di hook `before` dan `after`): Asset Class `B-EOLUSED` (dipakai 1 Asset Name dengan 5 aset aktif; Method `Declining Balance`, Useful Life 60, Declining Rate 40, End-of-Life Treatment `Switch to straight-line`; belum pernah diposting; tanpa versi Scheduled); Asset Class `B-EOLSCHED` (dipakai 1 Asset Name dengan 3 aset aktif; Method `Declining Balance`, Useful Life 60, Declining Rate 40, End-of-Life Treatment `Switch to straight-line`; tanpa versi Scheduled). Keduanya memakai Tax Depreciation Class `Bukan bangunan – Kelompok 1` dan Tax Method `Declining Balance`. Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Jam: M = bulan berjalan menurut zona waktu General Settings client (NC-11); jam server dan jam browser tidak digeser spec ini. Bulan pada Effective From dan Alert ditulis format `MMM yyyy`; asersi memakai M+n relatif terhadap M, bukan nama bulan literal.
- Data Dinamis: tidak ada. Spec mengubah End-of-Life Treatment `B-EOLUSED` (berlaku mulai M) dan `B-EOLSCHED` (versi Scheduled M+2); keduanya dipulihkan fixture BE, termasuk pembatalan versi Scheduled `B-EOLSCHED`.
- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca jumlah entri Changelog dibaca tepat sebelum aksi pemicu tiap TC (audit trail permanen, total tidak diturunkan dari seeding, S-12); fixture BE untuk seed dan pemulihan.
- State global: versi berlaku `B-EOLUSED` dan versi Scheduled `B-EOLSCHED` dipulihkan fixture BE di hook `after`; entri Changelog yang tercatat adalah audit trail permanen dan tidak dipulihkan.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di `suite.md`.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-FA-FAAC-724: Edit End-of-Life Treatment pada Asset Class yang dipakai aset menampilkan Apply Changes dan membentuk versi berlaku

1. Catat jumlah entri Changelog (Nc) sebagai baseline lewat kemampuan baca log
2. Ketik Search `B-EOLUSED`, tekan Enter
3. Klik link Class Code `B-EOLUSED` di tabel
4. Klik tab `Depreciation`
5. Ubah End-of-Life Treatment menjadi `Charge in final period`
6. Klik `Save`
7. Verifikasi dialog `Apply Changes` tampil
8. Verifikasi Effective From bernilai awal bulan berjalan (M)
9. Verifikasi checkbox `Apply to existing assets` tercentang
10. Verifikasi blok pratinjau `Assets affected` menampilkan 5
11. Pertahankan Effective From bulan berjalan, lalu klik `Apply`
12. Verifikasi halaman kembali ke tabel
13. Verifikasi toast sukses `Success, asset class has been updated.`
14. Ganti isi kotak search dengan `B-EOLUSED`, tekan Enter
15. Klik link Class Code `B-EOLUSED` di tabel
16. Klik tab `Depreciation`
17. Verifikasi End-of-Life Treatment `Charge in final period`
18. Verifikasi tidak ada Alert versi Scheduled
19. Klik breadcrumb `Asset Class`
20. Klik ikon Changelog di toolbar tabel (modal `Changelog: Asset Class`)
21. Verifikasi jumlah entri Changelog bertambah tepat 1 dari Nc
22. Verifikasi baris Changelog: Action `Edit`, Class Code `B-EOLUSED`, Field `End-of-Life Treatment`, Old Value `Switch to straight-line`, New Value `Charge in final period`, Modified By `Rina W`
23. Tutup modal Changelog

### TC-FA-FAAC-726: Edit End-of-Life Treatment dengan Effective From di masa depan menjadwalkan versi

24. Catat jumlah entri Changelog (Nc) sebagai baseline lewat kemampuan baca log
25. Ganti isi kotak search dengan `B-EOLSCHED`, tekan Enter
26. Klik link Class Code `B-EOLSCHED` di tabel
27. Klik tab `Depreciation`
28. Ubah End-of-Life Treatment menjadi `Keep depreciating`
29. Klik `Save`
30. Pilih Effective From dua bulan sesudah bulan berjalan (M+2)
31. Klik `Apply`
32. Verifikasi halaman tetap di Detail mode Edit
33. Verifikasi toast sukses tampil di halaman Detail: `Success, asset class has been updated.`
34. Verifikasi Alert info `Next version starts <M+2 dalam format MMM yyyy>.` tampil di atas bar tab
35. Klik tab `Depreciation`
36. Verifikasi tab Depreciation (terisi dari versi terakhir) menampilkan End-of-Life Treatment `Keep depreciating`
37. Klik breadcrumb `Asset Class`
38. Klik ikon Changelog di toolbar tabel (modal `Changelog: Asset Class`)
39. Verifikasi jumlah entri Changelog bertambah tepat 1 dari Nc
40. Verifikasi baris Changelog: Action `Edit`, Class Code `B-EOLSCHED`, Field `Scheduled Version`, Old Value `—`, New Value `<M+2 dalam format MMM yyyy>`
41. Verifikasi tidak ada baris Changelog dengan Field `End-of-Life Treatment` untuk `B-EOLSCHED` (versi belum berlaku)
42. Tutup modal Changelog

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-724, TC-FA-FAAC-726). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 dan 24 (baseline Changelog tiap TC, S-12), langkah 2 (Search untuk menemukan baris target, R-16 dan bagian 8b butir 13), langkah 14 dan 25 (Search ulang sesuai langkah TC; "ganti isi kotak search" karena kotak Search mempertahankan nilainya), langkah 19 dan 37 (kembali ke tabel lewat breadcrumb), langkah 23 dan 42 (menutup modal Changelog). Langkah 20 dan 38 membuka Changelog sebagai langkah observasi TC.
- Urutan asersi langkah 12 dan 13 mengikuti urutan state (bagian 8b butir 5): kembali ke tabel dan toast sukses mendahului asersi Detail; langkah 35 dan 36 mengikuti langkah TC-726 nomor 6.
- Asersi absence langkah 18 punya anchor positif langkah 17 (Detail termuat); asersi absence langkah 41 punya anchor positif langkah 40 pada surface yang sama (bagian 8b butir 2).
- Entri Changelog baru dibaca pada baris teratas urutan default `Date` terbaru setelah selisih jumlah dari baseline dibuktikan (S-14).
- Pengecualian nama literal (S-06, S-12; pengecualian beralasan yang disetujui user): `B-EOLUSED` dan `B-EOLSCHED` adalah seed bertanda `B-*` per TC yang dipakai apa adanya dan dipulihkan fixture BE.
- Alasan jumlah langkah: jumlah nominal melampaui sekitar 35 langkah; kedua blok TC satu topik (edit End-of-Life Treatment lewat Apply Changes) dan tiap blok memakai seed dan baseline sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain; blok baca-log berpola (buka Changelog lalu `Verifikasi` kolom log) tidak dihitung menurut bagian 3 smell.
- Temuan untuk QA: (a) TC-726 butir a menyebut toast di halaman Detail tanpa menyebut dialog tempat Effective From dipilih; spec mengikuti alur Save lalu Apply seperti spec versi Scheduled lain. (b) TC-724 butir d menyebut Modified By "aktor"; spec memakai nama tampil `Rina W` seperti spec log lain di suite ini. (c) TC-724 langkah 5 tidak menyebut label tombol dialog; spec memakai `Apply`.
