---
id: TC-GS-UOM-E2E-021-create-sukses-batas-trim-karakter-submit-dan-toast
title: "Create Unit Berhasil: Batas Karakter, Trim, Karakter Khusus, Symbol Duplikat, Perilaku Submit, dan Toast Beruntun"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-41
  - TC-GS-UOM-42
  - TC-GS-UOM-45
  - TC-GS-UOM-50
  - TC-GS-UOM-53
  - TC-GS-UOM-55
  - TC-GS-UOM-56
  - TC-GS-UOM-340
coverage:
  web: automated
---

# Create Unit Berhasil: Batas Karakter, Trim, Karakter Khusus, Symbol Duplikat, Perilaku Submit, dan Toast Beruntun

## Prerequisites

- Mode: FE+BE (backend nyata). Kasus saving state (TC-GS-UOM-56) memakai intercept parsial di atas backend nyata.
- Hook suite (login akun default Total Control Client A, `beforeEach` membuka Measurement, flag Guided Tooltip `guided_tooltip_seen_gs-measurement`): lihat `suite.md`. Password dari `Spectra.env.GS_TC_PASSWORD`; tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (data baca, tidak diubah): `Kilogram` / `kg` (Symbol `kg` dipakai ulang oleh TC-GS-UOM-53).
- Data dinamis (dibuat lewat UI oleh spec ini; nama bersuffix `{runId}-021` karena nama D-02 sampai D-11 dan D-30 dipakai lebih dari satu TC atau spec; nilai "tepat N karakter" dihitung termasuk suffix, S-12):

| TC | Data | Unit Name (input) | Symbol (input) |
|---|---|---|---|
| TC-GS-UOM-41 | D-02 | `  Hectare {runId}-021  ` (2 spasi depan dan belakang) | ` ha ` (spasi depan dan belakang) |
| TC-GS-UOM-42 | D-03 | 120 karakter: huruf `Z` diulang lalu ` {runId}-021` (total tepat 120) | `lu` |
| TC-GS-UOM-45 | D-04 | `Square Meter (m²) {runId}-021` | `m²` |
| TC-GS-UOM-50 | D-06 | `Kilowatt Hour {runId}-021` | `kWh-meter1` |
| TC-GS-UOM-53 | D-07 | `Kilogram Force {runId}-021` | `kg` |
| TC-GS-UOM-56 | D-11 | `Quart {runId}-021` | `qt` |
| TC-GS-UOM-340 | D-30 | `Stack 1 {runId}-021`, `Stack 2 {runId}-021`, `Stack 3 {runId}-021`, `Stack 4 {runId}-021` | `s1`, `s2`, `s3`, `s4` |
| TC-GS-UOM-55 | D-08 | `Barrel {runId}-021` | `bbl` |

- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): lepaskan semua intercept; hapus lewat API semua unit yang namanya memuat `{runId}-021`.
- Kemampuan teknis: `Spectra.intercept()` untuk menahan respons Create 2 detik dan melepasnya (TC-GS-UOM-56); klik ganda cepat pada [Submit]; hover pada tombol; submit empat unit berturut-turut dalam kurang dari 4 detik (TC-GS-UOM-340); pengukuran waktu hilangnya toast (4 detik, `foundation/functions/toast-copy.md` Aturan Terkunci #12); pembacaan teks sel tabel dan lebar kolom.
- State global: tidak ada yang diubah (intercept dilepas di langkah 33 dan di hook `after`).

## Test Steps

### TC-GS-UOM-41: Unit Name dan Symbol dengan spasi depan dan belakang disimpan ter-trim

1. Klik [+ Unit]
2. Centang checkbox `Stay on this form after submitting` agar form tetap terbuka untuk Create berikutnya
3. Isi Unit Name `  Hectare {runId}-021  ` dan Symbol ` ha `
4. Klik [Submit]
5. Verifikasi toast sukses: "Success, unit has been created."

### TC-GS-UOM-42: Unit Name tepat 120 karakter berhasil disimpan

6. Isi Unit Name 120 karakter (`Z` diulang ditambah ` {runId}-021`) dan Symbol `lu`
7. Verifikasi tidak ada error inline
8. Klik [Submit]
9. Verifikasi toast sukses: "Success, unit has been created."

### TC-GS-UOM-45: Unit Name dan Symbol berisi karakter cetak non-emoji diterima

10. Isi Unit Name `Square Meter (m²) {runId}-021` dan Symbol `m²`
11. Verifikasi tidak ada error inline
12. Klik [Submit]
13. Verifikasi toast sukses: "Success, unit has been created."

### TC-GS-UOM-50: Symbol tepat 10 karakter berhasil disimpan

14. Isi Unit Name `Kilowatt Hour {runId}-021` dan Symbol `kWh-meter1`
15. Verifikasi tidak ada error
16. Klik [Submit]
17. Verifikasi toast sukses: "Success, unit has been created."

### TC-GS-UOM-53: Symbol duplikat dengan unit lain diizinkan

18. Isi Unit Name `Kilogram Force {runId}-021` dan Symbol `kg`
19. Tunggu debounce ±500 ms
20. Verifikasi tidak ada error pada Symbol
21. Klik [Submit]
22. Verifikasi toast sukses: "Success, unit has been created."

### TC-GS-UOM-56: Tombol Submit masuk state proses dan klik ganda hanya membuat satu record

23. Pasang intercept yang menahan respons Create selama 2 detik
24. Isi Unit Name `Quart {runId}-021` dan Symbol `qt`
25. Arahkan kursor ke [Submit] tanpa mengklik
26. Verifikasi [Submit] menampilkan state hover yang berbeda dari state default
27. Klik [Submit] dua kali cepat
28. Verifikasi [Submit] menampilkan Saving state (spinner)
29. Verifikasi [Submit] disabled selama proses
30. Verifikasi [Clear Field] disabled
31. Verifikasi icon `[✕]` disabled
32. Verifikasi hanya satu toast sukses yang tampil: "Success, unit has been created."
33. Lepas intercept penahan respons

### TC-GS-UOM-340: Toast sukses beruntun: maksimal 3 toast tampil bersamaan, sisanya antri

34. Tunggu toast lama hilang otomatis
35. Submit 4 unit berturut-turut dalam waktu kurang dari 4 detik: `Stack 1 {runId}-021` / `s1`, `Stack 2 {runId}-021` / `s2`, `Stack 3 {runId}-021` / `s3`, `Stack 4 {runId}-021` / `s4`
36. Verifikasi paling banyak 3 toast `Success, unit has been created.` tampil bersamaan di kanan bawah
37. Verifikasi toast ke-4 antri dan tampil setelah salah satu toast hilang

### TC-GS-UOM-55: Submit Create dengan Stay unchecked menutup modal

38. Tunggu semua toast hilang otomatis
39. Lepas centang checkbox `Stay on this form after submitting`
40. Isi Unit Name `Barrel {runId}-021` dan Symbol `bbl`
41. Klik [Submit]
42. Verifikasi toast `Success, unit has been created.` tampil
43. Verifikasi toast tampil di kanan bawah
44. Verifikasi modal tertutup
45. Amati toast selama 6 detik
46. Verifikasi toast hilang otomatis setelah 4 detik (sudah tidak tampil pada detik ke-6)

### Verifikasi tabel setelah form ditutup (lanjutan TC-GS-UOM-41, 42, 53, 56, 340, 55)

47. Ketik Search `Hectare {runId}-021`, tekan Enter
48. Verifikasi Unit Name baris tampil `Hectare {runId}-021` dan Symbol `ha` tanpa spasi (TC-GS-UOM-41)
49. Ganti isi kotak search dengan nama Unit Name 120 karakter, tekan Enter
50. Verifikasi Unit Name 120 karakter tampil secara utuh (tidak dipotong `..`) (TC-GS-UOM-42)
51. Verifikasi kolom Unit Name melebar mengikuti konten (TC-GS-UOM-42)
52. Ganti isi kotak search dengan `kg`, tekan Enter
53. Verifikasi baris `Kilogram` dan baris `Kilogram Force {runId}-021` sama-sama bersymbol `kg` (TC-GS-UOM-53)
54. Ganti isi kotak search dengan `Quart {runId}-021`, tekan Enter
55. Verifikasi tepat satu baris `Quart {runId}-021` (TC-GS-UOM-56)
56. Ganti isi kotak search dengan `Stack`, tekan Enter
57. Verifikasi baris `Stack 1 {runId}-021`, `Stack 2 {runId}-021`, `Stack 3 {runId}-021`, dan `Stack 4 {runId}-021` tampil (TC-GS-UOM-340)
58. Ganti isi kotak search dengan `{runId}-021`, tekan Enter
59. Verifikasi baris `Barrel {runId}-021` berada di atas baris `Hectare {runId}-021` sesuai urutan Unit Name (TC-GS-UOM-55)
60. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 41, 42, 45, 50, 53, 56, 340 (satu sesi modal dengan Stay tercentang, prinsip 8 konvensi), lalu 55 (Stay dilepas sehingga Submit menutup form, sekaligus kejadian menutup form), lalu verifikasi tabel. Urutan menyimpang dari urutan TC sumber (41, 42, 45, 50, 53, 55, 56, 340) demi satu sesi modal; hanya satu kali [+ Unit] dibuka.
- Asersi "tampil di tabel" milik TC-GS-UOM-41, 42, 53, 56, 340, dan 55 ditaruh sesudah form ditutup (langkah 47 sampai 59) karena tabel berada di belakang modal selama Stay tercentang; toast dicek langsung sesudah Submit. TC-GS-UOM-45 dan 50 tidak punya Expected Result tampil di tabel.
- Langkah 59 (urutan Unit Name): Search `{runId}-021` memunculkan unit milik spec; `Barrel` mendahului `Hectare` pada urutan default A-Z. Urutan default tabel diasumsikan A-Z menurut Unit Name (TC-GS-UOM-55 Expected Result c).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 2 dan 39 (mengatur mode Stay, bukan asersi TC), langkah 23 dan 33 (memasang dan melepas intercept), langkah 34 dan 38 ("Tunggu toast lama hilang otomatis" sebelum menghitung toast), langkah 45 (mengamati toast 6 detik), serta langkah 47, 49, 52, 54, 56, 58, dan 60 (Search agar baris milik spec tampil di halaman aktif pada tabel 10 per halaman, lalu menutup Search).
- Nama dan Symbol memakai nilai TC dengan suffix `{runId}-021`; Symbol tidak bersuffix karena tidak unik (TC-GS-UOM-53).
- Spec memuat sekitar 60 langkah (melewati batas 35 langkah). Alasan: semua blok berada di satu kelas harness (Create sukses), satu akun, dan satu sesi modal; tiap Create memakai nama sendiri sehingga kegagalan satu Create tidak menghilangkan makna Create lain; memecah hanya menambah login, hook, dan pembukaan form.
- Parameter waktu: 2 detik (TC-GS-UOM-56) adalah parameter tahan respons Data Uji, bukan klaim PRD; 4 detik toast mengikuti `foundation/functions/toast-copy.md` Aturan Terkunci #12 (Success 4 detik).
- Temuan untuk QA:
  - TC-GS-UOM-42 menyebut "Unit Name 120 karakter (D-03)" tanpa jenis karakter; spec memakai huruf `Z` (diurutkan terakhir pada A-Z).
  - TC-GS-UOM-56 Expected Result a ("state hover yang berbeda dari state default") tidak menyebut properti visual; spec membandingkan state hover dengan state default tanpa nilai warna.
  - Post Condition TC-GS-UOM-41 sampai 56 ("Hectare / ha tersimpan ter-trim", dan seterusnya) tanpa langkah observasi terpisah selain Expected Result; hanya yang punya Expected Result yang diasersi.
  - TC-GS-UOM-340 Expected Result a dan b (paling banyak 3 toast `Success, unit has been created.` tampil bersamaan di kanan bawah, toast ke-4 antri) bertentangan dengan `foundation/functions/toast-copy.md` Aturan Terkunci (hanya 1 slot toast aktif di kanan bawah; toast baru menggantikan toast yang sedang tampil); langkah 36 dan 37 mengikuti TC.
